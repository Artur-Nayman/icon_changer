from flask import Flask, render_template, request, jsonify
import os
from main import change_existing_shortcut_icon

app = Flask(__name__)

icon_directory = r"C:\Users\artur\Documents\pycharm_projects\icon-changer\static\icons"

@app.route('/')
def index():
    try:
        icons = [f for f in os.listdir(icon_directory) if f.endswith('.ico')]
        return render_template('index.html', icons=icons)
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

        shortcut_path = os.path.join(r"C:\Users\artur\Desktop", f"{shortcut_name}.lnk")
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

if __name__ == '__main__':
    app.run(debug=True)
