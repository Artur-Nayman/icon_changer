import sys
import os

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

icon_directory = os.path.join(base_path, 'static', 'icons')
desktop_path = r"C:\Users\artur\Desktop"
