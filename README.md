Ось оновлений варіант твого `README.md`, що враховує нову функцію конвертації і видалення PNG файлів після створення ICO:

---

# Icon Changer Application

This application allows users to change the icons of their desktop shortcuts through a web interface. Users can select an icon from a list and apply it to a chosen shortcut. Additionally, the app supports automatic conversion of `.png` icons to `.ico` format and removes the original `.png` files after conversion.

## Features

* Display a list of available `.ico` icons (automatically converts `.png` files to `.ico`).
* Display a list of desktop shortcuts.
* Change the icon of a shortcut by selecting an icon and specifying the shortcut name.
* Automatically convert `.png` icons to `.ico` format and delete original `.png` files.

## Prerequisites

Before you begin, ensure you have the following installed:

* Python 3.6 or later
* Flask
* `pywin32` for Windows-specific functionality
* Pillow (`PIL`) for image processing

## Installation

1. **Clone the repository** (if applicable) or download the project files.

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install flask pywin32 pillow
   ```

4. **Configure the paths**:

   * Ensure the paths in `main.py` and `app.py` are set correctly to point to your icons directory and desktop.

## Usage

1. **Run the application**:

   Navigate to the directory containing `app.py` and run:

   ```bash
   python app.py
   ```

2. **Access the web interface**:

   Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Icon conversion**:

   When the app starts, it will automatically scan the icons directory for `.png` files, convert them to `.ico`, and delete the original `.png` files.

4. **Select an icon**:

   * Browse through the list of available `.ico` icons.
   * Click on an icon to select it.

5. **Choose a shortcut**:

   * View the list of desktop shortcuts in the right panel.
   * When prompted, enter the name of the shortcut you want to change.

6. **Change the icon**:

   * After selecting an icon and entering the shortcut name, the application will change the icon of the specified shortcut.

## Project Structure

* `app.py`: The main Flask application file that serves the web interface.
* `main.py`: Contains functions for scanning directories, changing shortcut icons, and converting icon files.
* 'config.py': Contains paths to desktop and icons directories
* `templates/`: Contains HTML templates for the web interface.

  * `index.html`: The main template for displaying icons and shortcuts.
* `static/icons/`: Directory containing the icon files.

## Troubleshooting

* Ensure all paths in the code are correct and point to the right directories on your system.
* Make sure you have the necessary permissions to change shortcut icons.
* Check that `.png` files in the icons directory are valid images.
* Check the console for any error messages if the application does not work as expected.

## License

This project is licensed under the MIT License.

---

Якщо хочеш, можу допомогти ще з автоматичним викликом `reformat_file` при запуску Flask, щоб конвертація відбувалась автоматично перед рендером сторінки.
