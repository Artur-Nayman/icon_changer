import win32com.client
import pythoncom
import os

def change_existing_shortcut_icon(shortcut_path, icon_path):
    if not os.path.exists(shortcut_path):
        print(f"Помилка: файл ярлика не існує за шляхом {shortcut_path}")
        return False
    if not os.path.exists(icon_path):
        print(f"Помилка: файл іконки не існує за шляхом {icon_path}")
        return False

    try:
        # Ініціалізуємо COM-бібліотеку
        pythoncom.CoInitialize()

        # Створюємо об'єкт WScript.Shell
        shell = win32com.client.Dispatch("WScript.Shell")

        # Завантажуємо існуючий ярлик
        shortcut = shell.CreateShortCut(shortcut_path)

        # Зміна іконки
        shortcut.IconLocation = icon_path
        shortcut.Save()

        print("Іконка успішно змінена.")
        return True
    except Exception as e:
        print(f"Помилка при зміні іконки: {e}")
        return False
    finally:
        # Завершуємо роботу з COM-бібліотекою
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
        print(f"Помилка при скануванні директорії: {e}")
        return []
