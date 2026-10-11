from auth.models import RegistrRequest, RegistrResponse, LoginRequest, LoginResponse, LogoutRequest, LogoutResponse, IsLoggedInRequest, IsLoggedInResponse

class Authorization:
    """Класс авторизации."""
    def __init__(
        self,
        csv_path: str
    ) -> None:
        """Проверка наличия файла."""
        ...

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
        ...

    def authentication(self, request: LoginRequest) -> LoginResponse:
        """Вход пользователя."""
        ...

    def log_out(self, request: LogoutRequest) -> LogoutResponse:
        """Выход пользователя."""
        ...

    def is_logged_in(self, request: IsLoggedInRequest) -> IsLoggedInResponse:
        """Проверка, авторизован ли пользователь."""
        ...
