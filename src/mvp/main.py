from datetime import datetime

def chat():
    user_name = "Salim"
    messages = []
    for i in range(4):
        message = input("Enter your message: ")
        time = datetime.now()
        messages.append(
            {
                "user": user_name,
                "message": message,
                "time": time,
            }
        )
    for item in messages:
        print(
            item["user"],
            f" ({item['time']})",
            ": ",
            item["message"],
            sep="",
        )

if __name__ == "__main__":
    chat()
