import csv          # Встроенный модуль для работы с CSV-файлами
import os           # Встроенный модуль для работы с файловой системой (проверка существования файла)
from datetime import datetime       # Импорт для работы с датой и временем

from model import Message

CSV_FILE = "messages.csv"         # Имя файла для хранения сообщений - messages.csv
chat_counter = 0                  # Счетчик чатов
COUNTER_FILE = "chat_counter.txt"    # Имя файла для счетчика

"""Фунция нахождения id чата"""
def get_next_chat_id() -> int:
    if not os.path.exists(CSV_FILE):        # проверяем, существует ли файл messages.csv
        return 1                    # Если файла нет возвращает 1 (первый чат)

    last_id = 0           # начальное значение (максимальный id)
    with open(                 # открываем файл для чтения
        CSV_FILE,
        "r",
        encoding="utf-8",
    ) as file:
        reader = csv.DictReader(file)          # читаем CSV как словарь. где ключи - названия столбцов
        for row in reader:          # перебираем все строки
            try:
                current_id = int(row["chat_id"])     # берем значение из столбца chat_id и превращаем в число
                last_id = max(last_id, current_id)   # оставляем максимальный id
            except (ValueError, KeyError):           # если строка битая - пропускаем
                print('Ошибка!')
                continue

        return last_id + 1          # возвращаем следующий id

"""Создание CSV-файла с заголовком, если его нет"""
def init_csv() -> None:
    if not os.path.exists(CSV_FILE):     # только если файла нет
        with open(CSV_FILE, "w",encoding='utf-8', newline="") as file:  # открываем для записи
            writer = csv.writer(file)         # создаем объект для записи CSV
            writer.writerow(["chat_id", "user", "message", "time"])    # пишем первую строку - заголовки столбцов

"""Функция сохранения сообщений в CSV формате"""
def save_message(
    message: Message,
) -> None:
    with open(CSV_FILE, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)              # объект для записи
        writer.writerow(message.row_fmt())     # вызываем метод row_fmt() у объекта Message и записываем результат
        # у класса Message должен быть метод row_fmt(), который возвращает список значений для CSV.

"""Функция создания чата"""
def chat():
    chat_id = get_next_chat_id()  # получаем ID для нового чата
    messages: list[Message] = []  # создаем пустой список для сообщений

    print(f"--- Чат #{chat_id} ---")   # выводим заголовок чата

    for i in range(4):     # Цикл 4 раза
        user_name = input("Enter a user name: ") # запрашиваем имя
        message = input("Enter a message: ")     # просим ввести сообщение
        time = datetime.now()         # текущее время
        messages.append(              # создаем объект Message и добавляем список
            Message(
                chat_id,
                user_name,
                message,
                time,
            )
        )
    for message in messages:   # перебираем все сообщения
        print(                      # выводим все без разделителя
            message.user_name,
            f" ({message.time})",
            ": ",
            message.message,
            sep="",
        )
        save_message(message)


if __name__ == "__main__":     # код выполняется, только если файл запущен напрямую
    init_csv()             # создаем CSV с заголовком (если его нет)
    chat()                # запускаем функцию
