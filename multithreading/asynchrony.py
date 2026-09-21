import asyncio


async def background_logger():
    while True:
        print("[Фон] Проверка статуса системы...")
        await asyncio.sleep(1)


async def main():
    # Создаем фоновую задачу (она начинает выполняться сразу)
    task = asyncio.create_task(background_logger())

    print("[Главный] Начало важной работы.")
    await asyncio.sleep(3.5)  # Имитируем основную работу
    print("[Главный] Важная работа завершена.")

    # Отменяем фоновую задачу, иначе она будет работать вечно
    task.cancel()


if __name__ == "__main__":
    asyncio.run(main())