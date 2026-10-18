from .models import CreateCorrespondenceRequest, CreateCorrespondenceResponse, SendMessageRequest, SendMessageResponse, GetCorrespondenceRequest, GetCorrespondenceResponse
from pathlib import Path
from ..models import CorrespondenceModel
from csv import DictWriter

COLUMNS = CorrespondenceModel.__slots__


class CorrespondenceManager:
    def __init__(
        self,
        correspondence_path: Path
    ) -> None:
        self._correspondence_path = correspondence_path
        self._create_csv()

    def _create_csv(self) -> None:
        """Создание csv-файла, если его ещё нет."""
        if not self._correspondence_path.exists():
            print(f"Файл {self._correspondence_path} не создан, создаём.")
            with self._correspondence_path.open(mode="w", encoding="utf-8", newline="") as file:
                current_writer = DictWriter(file, fieldnames=COLUMNS)
                current_writer.writeheader()
                return
        print(f"Файл {self._correspondence_path} уже существует.")

    def create_correspondence(
        self,
        request: CreateCorrespondenceRequest,
    ) -> CreateCorrespondenceResponse:
        """
        Создание переписки.

        Что ожидается:
            1. Проверить, существует ли уже переписка?
                - Если уже существует, то нужно вернуть её идентификатор.
            2. Если переписка не существует, то создаём её.
            3. Фиксируем в csv эту переписку.
            4. Возвращаем ответ об успешности.
        """
        ...

    def send_message(
        self,
        request: SendMessageRequest,
    ) -> SendMessageResponse:
        """
        Отправка сообщения.

        Что ожидается:
            1. Проверка наличия пользователя в переписке.
                - Если его нет, то вернуть соответствующий ответ.
            2. Если пользователь уже есть, то добавить сообщение в переписку.
        """
        ...

    def get_correspondence(
        self,
        request: GetCorrespondenceRequest,
    ) -> GetCorrespondenceResponse:
        """Получение переписки."""
        ...
