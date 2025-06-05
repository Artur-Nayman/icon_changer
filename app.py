from flask import Flask, render_template, request, jsonify
import os
from main import change_existing_shortcut_icon, scan_directory, reformat_file
from config import icon_directory, desktop_path
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    try:
        # Запускаємо обробку файлів перед відображенням
        icon_files = [f for f in os.listdir(icon_directory) if f.endswith(('.ico', '.png'))]
        reformat_file(icon_files, icon_directory)

        # Тепер вже зчитуємо лише .ico
        icons = [f for f in os.listdir(icon_directory) if f.endswith('.ico')]
        shortcuts = scan_directory(desktop_path)
        return render_template('index.html', icons=icons, shortcuts=shortcuts)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/select_icon', methods=['POST'])
def select_icon():
    try:
        data = request.json
        selected_icon = data.get('icon')
        shortcut_name = data.get('shortcut')

        if not selected_icon or not shortcut_name:
            return jsonify({"status": "error", "message": "Icon or shortcut name not provided"}), 400

        shortcut_path = os.path.join(desktop_path, f"{shortcut_name}.lnk")
        icon_path = os.path.join(icon_directory, selected_icon)

        if not os.path.exists(shortcut_path):
            return jsonify({"status": "error", "message": f"Shortcut does not exist: {shortcut_path}"}), 404

        if not os.path.exists(icon_path):
            return jsonify({"status": "error", "message": f"Icon does not exist: {icon_path}"}), 404

        success = change_existing_shortcut_icon(shortcut_path, icon_path)

        if success:
            return jsonify({"status": "success", "icon": selected_icon, "shortcut": shortcut_name})
        else:
            return jsonify({"status": "error", "message": "Failed to change icon"}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/download_icon', methods=['POST'])
def download_icon():
    data = request.get_json()
    icon_url = data.get('icon_url')

    if not icon_url:
        return jsonify({"message": "URL не вказано"}), 400

    try:
        icon_name = os.path.basename(icon_url)
        save_path = os.path.join(icon_directory, icon_name)

        response = requests.get(icon_url)
        response.raise_for_status()

        with open(save_path, 'wb') as f:
            f.write(response.content)

        return jsonify({"message": f"Іконка '{icon_name}' збережена!"})

    except Exception as e:
        return jsonify({"message": f"Помилка: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
