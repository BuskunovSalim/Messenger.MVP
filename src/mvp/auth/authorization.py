from auth.models import RegistrRequest, RegistrResponse, LoginRequest, LoginResponse, LogoutRequest, LogoutResponse, IsLoggedInRequest, IsLoggedInResponse
import csv
import os
import hashlib
from datetime import datetime


class Authorization:
    """Класс авторизации."""
    FIELDS = ['user_id', 'username', 'password_hash', 'is_logged_in', 'created_at']
    def __init__(
        self,
        csv_path: str
    ) -> None:
        """Проверка наличия файла."""
        self.csv_path = csv_path
        self._init_csv()

    def _init_csv(self) -> None:
        """Создаём CSV с заголовком, если файла нет."""
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.FIELDS)

    def _read_all(self) -> list[dict]:
        """Читаем всех пользователей как список словарей."""
        with open(self.csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def _write_all(self, users: list[dict]) -> None:
        """Перезаписываем файл пользователей."""
        with open(self.csv_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.FIELDS)
            writer.writeheader()
            writer.writerows(users)

    @staticmethod       # декоратор, который превращает метод класса в обычную функцию, не привязанную ни к объекту, ни к классу.
    def _hash_password(password: str) -> str:
        """Хешируем пароль."""
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def _next_user_id(self, users: list[dict]) -> int:
        """Возвращаем следующий свободный user_id."""
        if not users:
            return 1
        return max(int(u['user_id']) for u in users) + 1

    def _find_user(self, users: list[dict], username: str) -> dict | None:
        """Ищем пользователя по имени."""
        for user in users:
            if user['username'] == username:
                return user
        return None


    def registration(
        self,
        request: RegistrRequest
    ) -> RegistrResponse:
        """
        Добавляем нового пользователя.
        Что делает:
            # Проверяет уникальность имени.
            # Сохраняет данные по пользователю.
            # Выдаёт идентификатор пользователя.
        """


    def authentication(self, request: LoginRequest) -> LoginResponse:
        """Вход пользователя."""
        ...

    def log_out(self, request: LogoutRequest) -> LogoutResponse:
        """Выход пользователя."""
        ...

    def is_logged_in(self, request: IsLoggedInRequest) -> IsLoggedInResponse:
        """Проверка, авторизован ли пользователь."""
        ...
