from multiprocessing import Process
from multiprocessing.managers import BaseManager
import time

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item: str, quantity: int):
        if item not in self.items:
            self.items[item] = quantity
        else:
            self.items[item] += quantity
        print(f"[Storage] Added {item} to inventory, quantity {quantity}.")
    def get_stock(self) -> dict:
        return self.items


class CustomManager(BaseManager):
    pass

def worker_task(shared_inventory, item_name, quantity):
    print(f"[Процесс {item_name}] Начинает работу...")
    time.sleep(1)  # Имитация работы
    shared_inventory.add_item(item_name, quantity)
    print(f"[Процесс {item_name}] Завершил добавление.")


if __name__ == "__main__":
    # Регистрируем наш класс в менеджере под именем "Inventory"
    CustomManager.register("Inventory", Inventory)
    with CustomManager() as manager:
        # Создаем общий объект через менеджер
        # Внутри менеджера создается реальный Inventory, а нам возвращается прокси
        shared_inventory = manager.Inventory()

        # Для демонстрации создаем два процесса и передаем им наш прокси-объект
        p1 = Process(target=worker_task, args=(shared_inventory, "Яблоки", 10))
        p2 = Process(target=worker_task, args=(shared_inventory, "Бананы", 5))

        p1.start()
        p2.start()

        # Ждем завершения процессов
        p1.join()
        p2.join()

        # Проверяем финальное состояние объекта в главном процессе
        print("\n--- Финальный отчет о складе ---")
        print(shared_inventory.get_stock())