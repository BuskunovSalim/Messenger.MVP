from datetime import datetime
import csv
import os

CSV_FILE = 'messages.csv'
chat_counter = 0
COUNTER_FILE = 'chat_counter.txt'


def get_next_chat_id() -> int:
    if not os.path.exists(CSV_FILE):
        return 1

    last_id = 0
    with open(CSV_FILE, 'r', encoding='utf-8',) as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                current_id = int(row['chat_id'])
                last_id = max(last_id, current_id)
            except (ValueError, KeyError):
                continue

        return last_id + 1

def init_csv() -> None:
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['chat_id', 'user', 'message', 'time'])

def save_message(chat_id: str, user_name: str, message: str, time: datetime) -> None:
    with open(CSV_FILE, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([chat_id, user_name, message, time.strftime('%Y-%m-%d %H:%M:%S')])

def chat():
    chat_id = get_next_chat_id()
    messages = []

    print(f'--- Чат #{chat_id}---')

    for i in range(4):
        user_name = input('Enter a user name: ')
        message = input('Enter a message: ')
        time = datetime.now()
        messages.append(
            {
                'chat_id': chat_id,
                'user': user_name,
                'message': message,
                'time': time,
            }
        )
    for item in messages:
        print(
            item['user'],
            f" ({item['time']})",
            ': ',
            item['message'],
            sep='',
            )
        save_message(
            item['chat_id'],
            item['user'],
            item['message'],
            item['time'],
        )





if __name__=='__main__':
    init_csv()
    chat()
