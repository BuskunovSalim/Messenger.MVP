from datetime import datetime
from enum import StrEnum, auto
from dataclasses import dataclass, asdict
from typing import Self


@dataclass(slots=True)
class UserModel:
    login: str
    password: str
    identifier: int

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(
            login=data["login"],
            password=data["password"],
            identifier=int(data["identifier"]),
        )

    def dict_fmt(self) -> dict:
        return asdict(self)

@dataclass(slots=True)
class MessageStatus(StrEnum):
    """Статусы сообщений."""
    ERROR = auto()
    SENT = auto()
    IN_TRANSIT = auto()
    RECEIVED = auto()
    VIEWED = auto()

@dataclass(slots=True)
class MessageModel:
    """Модель сообщения."""
    identifier: int
    status: MessageStatus
    text: str
    time_sending: datetime
    status: MessageStatus

@dataclass(slots=True)
class CorrespondenceModel:
    """Модель переписки."""
    identifier: int
    messages: list[MessageModel]
    users: list[UserModel]
