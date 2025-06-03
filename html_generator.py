import os

def generate_html(files, output_dir, output_file):
    """
    Генерує HTML файл з переліком наданих файлів.

    Аргументи:
        files (list): Список імен файлів, які будуть включені в HTML.
        output_dir (str): Директорія, куди буде збережено HTML файл.
        output_file (str): Назва HTML файлу, який буде створено.
    """
    # Перевіряємо, чи існує директорія для виводу, і створюємо її, якщо вона не існує
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Формуємо повний шлях для вихідного HTML файлу
    full_path = os.path.join(output_dir, output_file)

    # Починаємо будувати вміст HTML з базової структури
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Files List</title>
    </head>
    <body>
        <h1>Files List</h1>
        <ul>
    """

    # Ітеруємося по кожному файлу у списку та додаємо його як елемент списку в HTML
    for file in files:
        # Додаємо кожен файл як елемент списку
        html_content += f"            <li>{file}</li>\n"

    # Правильно закриваємо HTML теги
    html_content += """
        </ul>
    </body>
    </html>
    """

    # Записуємо згенерований HTML вміст у вказаний файл
    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
