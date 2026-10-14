from dataclasses import dataclass


@dataclass              #Ваще читы, атоматически создает конструктор, строковое представление и сравнение
class RegistrRequest:
    """Запрос на регистрацию."""
    login: str
    password: str

@dataclass
class RegistrResponse:
    """Результат регистрации."""
    success: bool
    message: str
    user_id: int | None = None

@dataclass
class LoginRequest:
    """Запрос на вход"""
    login: str
    password: str

@dataclass
class LoginResponse:
    """Результат входа"""
    success: bool
    message: str
    user_id: int | None = None

@dataclass
class LogoutRequest:
    """Запрос на выход"""
    user_id: int

@dataclass
class LogoutResponse:
    """Результат выхода"""
    success: bool
    message: str

@dataclass
class IsLoggedInRequest:
    """Запрос на проверку статуса входа"""
    user_id: int

@dataclass
class IsLoggedInResponse:
    """Результат проверки статуса"""
    is_logged_in: bool
    login: str | None = None
