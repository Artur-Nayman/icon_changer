import sys
import os
import ctypes
from ctypes import wintypes

def resource_path(relative_path):
    """Повертає абсолютний шлях до ресурсу, працює в .py та .exe"""
    try:
        # PyInstaller створює тимчасову директорію та зберігає шлях у _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Шлях до директорії з іконками
icon_directory = resource_path(os.path.join("static", "icons"))

def get_desktop_path():
    """Повертає шлях до робочого столу"""
    CSIDL_DESKTOPDIRECTORY = 0x10
    buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOPDIRECTORY, None, 0, buf)
    return buf.value

# Шлях до ярликів на робочому столі
desktop_path = get_desktop_path()
