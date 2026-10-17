from email import message

from auth.models import RegistrRequest, RegistrResponse, LoginRequest, LoginResponse, LogoutRequest, LogoutResponse, IsLoggedInRequest, IsLoggedInResponse
from pathlib import Path
from csv import DictWriter, DictReader

COLUMNS = ["login", "password", "identifier"]

sample = {
    "login": "Salim",
    "password": "Secret",
    "identifier": "1",
}

class Authorization:
    """Класс авторизации."""
    def __init__(
        self,
        csv_path: Path
    ) -> None:
        """Проверка наличия файла."""
        self._csv_path = csv_path
        self._create_csv()
        self.authorized_users = set()

    def _create_csv(self) -> None:
        """Создание csv-файла, если его ещё нет."""
        if not self._csv_path.exists():
            print(f"Файл {self._csv_path} не создан, создаём.")
            with self._csv_path.open(mode="w", encoding="utf-8", newline="") as file:
                current_writer = DictWriter(file, fieldnames=COLUMNS)
                current_writer.writeheader()
                return
        print(f"Файл {self._csv_path} уже существует.")

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
        current_users = self._read_csv()
        locked_logins = set()
        for user in current_users:
            locked_logins.add(user["login"])
        if request.login in locked_logins:
            message = f"Логин {request.login} уже занят."
            print(message)
            return RegistrResponse(
                success=False,
                message=message,
                user_id=None,
            )
        identifier = len(locked_logins) + 1
        with self._csv_path.open(mode="a", encoding="utf-8", newline="") as file:
            writer = DictWriter(file, fieldnames=COLUMNS)
            writer.writerow(
                {
                    "login": request.login,
                    "password": request.password,
                    "identifier": identifier
                }
            )
        message = "Успешно авторизован."
        print(message)
        return RegistrResponse(
            success=True,
            message=message,
            user_id=identifier,
        )

    def _read_csv(self) -> list[dict]:
        users = []
        with self._csv_path.open(mode="r", encoding="utf-8", newline="") as file:
            reader = DictReader(file, fieldnames=COLUMNS)
            next(reader)
            for row in reader:
                users.append(row)
        return users

    def authorization(self, request: LoginRequest) -> LoginResponse:
        """
        Вход пользователя.

        Что ожидается:
            1. На вход получаем модель LoginRequest (уже сделано).
            2. Загружаем в память список всех пользователей.
            3. В списке всех пользователей ищем пользователя с переданным логинов request.login
                - Если такого пользователя нет, то возвращаем модель LoginResponse,
                в которой success=False, message="Такого пользователя нет. (указать login)",
                user_id=None.
            4. Если пользователь есть, то проверить его user_id в списке уже авторизованных
            с помощью is_logged_in.
                - Если пользователь авторизован, то вернуть ответ, в котором
                success=True, message="Пользователь {его логин} уже авторизован.",
                user_id=<его user_id>.
            5. Если пользователь ещё не авторизован, то проверяем правильность пароля.
                - Если пароль неправильный, то вернуть соответствующий ответ как в пункте 3,
                но с другим сообщением.
            6. Если пароль правильный, то добавляем user_id в множество авторизованных.
            7. Возвращаем корректный ответ success=True,
            message="Пользователь {его логин} успешно авторизован.", user_id=<его user_id>.
        """
        ...

    def log_out(self, request: LogoutRequest) -> LogoutResponse:
        """
        Выход пользователя.

        Что ожидается:
            1. На вход получаем модель LogoutRequest (уже сделано).
            2. Проверяем, есть ли user_id в множестве авторизованных.
                - Если его нет, то возвращаем success=True,
                message="Пользователь не быд авторизован".
            3. Если пользователь уже был авторизован, то удаляем его из множества авторизованных
                пользователей.
            4. Возвращаем ответ LogoutResponse(success=True, message=f"Пользователь {request.user_id}
            успешно разлогирован.")
        """
        ...

    def is_logged_in(self, request: IsLoggedInRequest) -> IsLoggedInResponse:
        """
        Проверка, авторизован ли пользователь.

        Что ожидается:
            1. Проверяем, есть ли user_id в множестве авторизованных.
            2. Возвращаем ответ.
        """
        ...
