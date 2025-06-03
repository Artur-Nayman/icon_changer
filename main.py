import win32com.client
import os

# Шляхи папок
desktop = r"C:\Users\artur\Desktop\\"
icon = r"C:\Users\artur\Pictures\icon-changer\\"
directory_path = r"C:\Users\artur\Pictures\icon-changer"
desktop_path = r"C:\Users\artur\Desktop"

#Функція зміни іконки
def change_existing_shortcut_icon(shortcut_path, icon_path):
    # Перевірка існування ярлика та іконки
    if not os.path.exists(shortcut_path):
        print(f"Помилка: файл ярлика не існує за шляхом {shortcut_path}")
        return
    if not os.path.exists(icon_path):
        print(f"Помилка: файл іконки не існує за шляхом {icon_path}")
        return

    try:
        # Створюємо об'єкт WScript.Shell
        shell = win32com.client.Dispatch("WScript.Shell")

        # Завантажуємо існуючий ярлик
        shortcut = shell.CreateShortCut(shortcut_path)

        # Зміна іконки
        shortcut.IconLocation = icon_path
        shortcut.Save()

        print("Іконка успішно змінена.")
    except Exception as e:
        print(f"Помилка при зміні іконки: {e}")



#Сканування об'єктів
def scan_directory(directory_path):
    try:
        # Отримуємо список усіх файлів та папок у вказаній директорії
        files_and_dirs = os.listdir(directory_path)

        # Фільтруємо тільки файли з розширеннями .ico та .lnk та видаляємо розширення
        files = [os.path.splitext(f)[0] for f in files_and_dirs
                 if os.path.isfile(os.path.join(directory_path, f)) and
                 f.lower().endswith(('.ico', '.lnk'))]

        return files
    except Exception as e:
        return str(e)

# Вивід списку
files = scan_directory(directory_path)
files2 = scan_directory(desktop_path)

print("Файли у папці:", files)
print("Файли у папці:", files2)

#Вкажіть шлях
shortcut_path = desktop + input("Вкажіть назву ярлика:") + ".lnk"  # Вкажіть шлях до існуючого ярлика
icon_path = icon + input("Вкажіть назву іконки:") + ".ico"  # Вкажіть шлях до нового файлу іконки

change_existing_shortcut_icon(shortcut_path, icon_path)

