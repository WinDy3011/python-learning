from multiprocessing import Process, Pipe


# функция, которая запускается во втором процессе
def conn1_func(conn):
    n = 5
    conn.send(n)  # посылаем число
    square_n = conn.recv()  # получаем из квадрат числа
    conn.close()  # закрываем канал
    print(f"Квадрат числа {n} равен {square_n}")


def conn2_func(conn):
    n = conn.recv()  # получаем из канала число
    conn.send(n * n)  # посылаем обратно квадрат числа


if __name__ == "__main__":
    conn1, conn2 = Pipe()

    # определяем и запускаем два процесса для каждой из сторон канала
    conn1_process = Process(target=conn1_func, args=(conn1,))
    conn2_process = Process(target=conn2_func, args=(conn2,))

    conn1_process.start()
    conn2_process.start()

    conn1_process.join()
    conn2_process.join()