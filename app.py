from flask import Flask, render_template, request, jsonify
import os
from main import change_existing_shortcut_icon

app = Flask(__name__)

icon_directory = r"C:\Users\artur\Documents\pycharm_projects\icon-changer\static\icons"

@app.route('/')
def index():
    icons = [f for f in os.listdir(icon_directory) if f.endswith('.ico')]
    return render_template('index.html', icons=icons)

@app.route('/select_icon', methods=['POST'])
def select_icon():
    data = request.json
    selected_icon = data.get('icon')
    shortcut_name = data.get('shortcut')

    shortcut_path = os.path.join(r"C:\Users\artur\Desktop", f"{shortcut_name}.lnk")
    icon_path = os.path.join(icon_directory, selected_icon)

    change_existing_shortcut_icon(shortcut_path, icon_path)

    return jsonify({"status": "success", "icon": selected_icon, "shortcut": shortcut_name})

if __name__ == '__main__':
    app.run(debug=True)
