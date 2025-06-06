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
