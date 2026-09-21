import threading
import time

x = 0  # общий ресурс

x_lock = threading.Lock()  # Создаем объект блокировки

threads = []  # список потоков


def increase_x():
    global x
    thread_name = threading.current_thread().name  # имя текущего потока

    # Менеджер with сам вызовет acquire() и release()
    with x_lock:
        x = 1  # устанавливаем новое значение для общего ресурса
        for _ in range(1, 4):
            print(f"{thread_name}: {x}")
            x += 1  # изменение общего ресурса
            time.sleep(0.5)  # имитация работы


# запускаем три потока
for i in range(1, 4):
    my_thread = threading.Thread(target=increase_x, name=f"Поток {i}")
    threads.append(my_thread)
    my_thread.start()  # запускаем потоки

# ожидаем завершения потоков
for my_thread in threads:
    my_thread.join()