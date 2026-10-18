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
