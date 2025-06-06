import win32com.client
import pythoncom
import os
from PIL import Image
from config import icon_directory

def change_existing_shortcut_icon(shortcut_path, icon_path):
    if not os.path.exists(shortcut_path):
        print(f"Error: Shortcut file does not exist at path {shortcut_path}")
        return False
    if not os.path.exists(icon_path):
        print(f"Error: Icon file does not exist at path {icon_path}")
        return False

    try:
        # Initialize the COM library
        pythoncom.CoInitialize()

        # Create a WScript.Shell object
        shell = win32com.client.Dispatch("WScript.Shell")

        # Load the existing shortcut
        shortcut = shell.CreateShortCut(shortcut_path)

        # Change the icon
        shortcut.IconLocation = icon_path
        shortcut.Save()

        print("Icon changed successfully.")
        return True
    except Exception as e:
        print(f"Error while changing the icon: {e}")
        return False
    finally:
        # Uninitialize the COM library
        pythoncom.CoUninitialize()

def scan_directory(directory_path):
    try:
        files_and_dirs = os.listdir(directory_path)
        files = [
            os.path.splitext(f)[0] for f in files_and_dirs
            if os.path.isfile(os.path.join(directory_path, f)) and f.lower().endswith(('.ico', '.lnk'))
        ]
        return files
    except Exception as e:
        print(f"Error while scanning the directory: {e}")
        return []

def reformat_file(files, icon_directory):
    for file in files:
        if file.endswith(('.ico', '.png')):
            file_path = os.path.join(icon_directory, file)
            img = Image.open(file_path)
            img = img.convert('RGBA')
            new_path = os.path.splitext(file_path)[0] + '.ico'
            img.save(new_path, format='ICO')
            if file.lower().endswith('.png'):
                os.remove(file_path)
                print(f"Original PNG deleted: {file_path}")
