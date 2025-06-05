import sys
import os
import ctypes
from ctypes import wintypes

# Визначаємо базовий шлях
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# Директорія іконок
icon_directory = os.path.join(base_path, 'static', 'icons')

def get_desktop_path():
    CSIDL_DESKTOPDIRECTORY = 0x10
    buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOPDIRECTORY, None, 0, buf)
    return buf.value

# Приклад використання
desktop_path = get_desktop_path()
print("Desktop path:", desktop_path)