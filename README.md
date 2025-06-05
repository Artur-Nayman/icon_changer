# Icon Changer Application

This application allows users to change the icons of their desktop shortcuts through a web interface. Users can select an icon from a list and apply it to a chosen shortcut.

## Features

- Display a list of available icons.
- Display a list of desktop shortcuts.
- Change the icon of a shortcut by selecting an icon and specifying the shortcut name.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or later
- Flask
- `pywin32` for Windows-specific functionality

## Installation

1. **Clone the repository** (if applicable) or download the project files.

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install flask pywin32
   ```

4. **Configure the paths**:

   - Ensure the paths in `main.py` and `app.py` are set correctly to point to your icons directory and desktop.

## Usage

1. **Run the application**:

   Navigate to the directory containing `app.py` and run:

   ```bash
   python app.py
   ```

2. **Access the web interface**:

   Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Select an icon**:

   - Browse through the list of available icons.
   - Click on an icon to select it.

4. **Choose a shortcut**:

   - View the list of desktop shortcuts in the right panel.
   - When prompted, enter the name of the shortcut you want to change.

5. **Change the icon**:

   - After selecting an icon and entering the shortcut name, the application will change the icon of the specified shortcut.

## Project Structure

- `app.py`: The main Flask application file that serves the web interface.
- `main.py`: Contains functions for scanning directories and changing shortcut icons.
- `templates/`: Contains HTML templates for the web interface.
  - `index.html`: The main template for displaying icons and shortcuts.
- `static/icons/`: Directory containing the icon files.

## Troubleshooting

- Ensure all paths in the code are correct and point to the right directories on your system.
- Make sure you have the necessary permissions to change shortcut icons.
- Check the console for any error messages if the application does not work as expected.

## License

This project is licensed under the MIT License.

### Explanation:

- **Prerequisites**: Lists the necessary software and libraries required to run the application.
- **Installation**: Provides steps to set up the environment and install dependencies.
- **Usage**: Describes how to run the application and use its features.
- **Project Structure**: Explains the organization of the project files.
- **Troubleshooting**: Offers tips for resolving common issues.
- **License**: Specifies the license under which the project is distributed.

You can customize this `README.md` further based on additional details or specific instructions related to your project setup.
