import threading
import time


# условная функция загрузки файла
def download_file(file_id):
    print(f"Скачивание файла {file_id}...")
    time.sleep(2)
    print(f"Файл {file_id} успешно скачан!")


# список потоков
threads = []

# Создаем и запускаем 3 потока
for i in range(1, 4):
    t = threading.Thread(target=download_file, args=(i,))
    threads.append(t)
    t.start()

# дожидаемся завершения КАЖДОГО потока
for t in threads: t.join()

print("Все файлы скачаны!")