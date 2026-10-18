from pprint import pprint

from auth.authorization import Authorization
from auth.models import RegistrRequest, LoginRequest

from pathlib import Path

def main():
    path = Path("users.csv")
    auth = Authorization(path)
    registr = RegistrRequest(
        login="kolya",
        password="1234",
    )
    auth.registration(registr)
    response = auth.authorization(
        LoginRequest(
            login="kolya",
            password="1234",
        )
    )
    pprint(response)



if __name__ == "__main__":
    main()
