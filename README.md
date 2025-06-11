# Icon Manager Flask App

A web application for downloading, browsing, and applying icons to Windows desktop shortcuts.

---

## Description

This project allows you to:

* Download icons from a remote GitHub repository to the local `static/icons/` folder.
* Browse icons by categories.
* Search icons by name.
* Apply selected icons to existing Windows desktop shortcuts.
* Store icons locally so they persist after application restarts.
* Project is connected t othis website https://github.com/Artur-Nayman/icon-db-wesite

---

[![Discussions](https://img.shields.io/github/discussions/Artur-Nayman/personal-portfolio?label=Discuss%20on%20GitHub&logo=github)](https://github.com/Artur-Nayman/personal-portfolio/discussions)
[![Try it now](https://img.shields.io/badge/Try%20it%20now-Demo-blue)](https://youtu.be/Rr20QJncsy4)
[![Show on Product Hunt](https://img.shields.io/badge/ProductHunt-Show%20on%20PH-red?logo=producthunt)](https://www.producthunt.com/posts/your-project-slug)

---

## 🎥 Demo

[![Watch the video](https://img.youtube.com/vi/Rr20QJncsy4/maxresdefault.jpg)](https://youtu.be/Rr20QJncsy4)

👉 Click the image to watch a short demo on YouTube.

---

## 🚀 Features

- Web interface to browse and apply icons
- Installs icons directly to the correct system folder
- Auto-detects your desktop shortcuts
- Replace icons with one click
- Supports custom icons you drag & drop into the folder

---

## 📦 Installation
Just download from releases setup file
or
1. Clone the repo
2. Run the local server
3. Open the web UI in your browser
4. Choose and apply icons

---

## 💬 Feedback

Have ideas or bugs to report? [Start a discussion](https://github.com/Artur-Nayman/personal-portfolio/discussions) or open an issue!

---

## 🐱 GitHub Discussions

Want to share your thoughts or ask for feedback?
👉 Visit the [Discussions tab](https://github.com/Artur-Nayman/personal-portfolio/discussions)

---

## Technologies Used

* Python 3.x
* Flask
* Requests
* Flask-CORS
* JavaScript (frontend)
* HTML/CSS

---

## Project Structure

```
/static/icons/        # Folder with icons
/templates/index.html # Main web interface
app.py                # Main Flask application
main.py               # Logic for changing shortcut icons, scanning directories, and file formatting
config.py             # Configuration (paths)
```

---

## Installation and Running

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

4. Open in your browser at [http://localhost:5000](http://localhost:5000)

---

## Usage

* You can find icons from catalog page which is released on github.
* Select icon categories using the tabs.
* Click the "Install" button to download the icon to the local folder.
* Choose a desktop shortcut and apply the icon to it.

---

## Configuration

* Paths are set in `config.py`:

  ```python
  icon_directory = os.path.join(base_path, 'static', 'icons')
  desktop_path = get_desktop_path()
  ```

* Adjust `reformat_file()` in `main.py` if needed to prevent icons from being removed after download.

---

## Notes

* Ensure the folder `static/icons/` exists and is writable.
* Icons in `.ico` format display correctly and persist between sessions.
* The app is Windows-only, as it manipulates `.lnk` shortcut files.

---

## License

This project is licensed under the MIT License.
