import random


def generate_file(file_path, total_lines=1_000_000):
    # Варианты логов для генерации
    log_templates = [
        "[INFO] User logged in successfully.",
        "[INFO] Page loaded in 24ms.",
        "[WARNING] Database connection slow.",
        "[INFO] API request completed.",
        "[ERROR] Failed to connect to database!",
        "[ERROR] User authentication timeout."
    ]

    print(f"Начинаю генерацию файла {file_path}...")

    # Открываем файл для записи ("w")
    with open(file_path, "w", encoding="utf-8") as file:
        for i in range(total_lines):
            # Случайно выбираем один шаблон
            log_entry = random.choice(log_templates)
            # Записываем строку, добавляя индекс и перенос строки \n
            file.write(f"Line {i + 1}: {log_entry}\n")

    print(f"Готово! Файл {file_path} успешно создан.")


file_path = "server_logs.txt"



generate_file(file_path, total_lines=1_000_000)