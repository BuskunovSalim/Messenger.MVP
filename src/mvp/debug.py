from auth.authorization import Authorization
from auth.models import RegistrRequest

from pathlib import Path

def main():
    path = Path("users.csv")
    auth = Authorization(path)
    registr = RegistrRequest(
        login="kolya",
        password="1234"
    )
    auth.registration(registr)


if __name__ == "__main__":
    main()
