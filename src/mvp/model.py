from datetime import datetime
class Message:
    """Класс сообщений."""
    def __init__(self, chat_id: int, user_name: str, message: str, time: datetime ) -> None:
        self.chat_id = chat_id
        self.user_name = user_name
        self.message = message
        self.time = time