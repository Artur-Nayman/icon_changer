import sys
import os
import ctypes
from ctypes import wintypes

def resource_path(relative_path):
    """Returns the absolute path to a resource, works in both .py and .exe"""
    try:
        # PyInstaller creates a temporary folder and stores the path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Path to the directory containing icons
icon_directory = resource_path(os.path.join("static", "icons"))

def get_desktop_path():
    """Returns the path to the desktop"""
    CSIDL_DESKTOPDIRECTORY = 0x10
    buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOPDIRECTORY, None, 0, buf)
    return buf.value

# Path to the desktop shortcuts
desktop_path = get_desktop_path()
