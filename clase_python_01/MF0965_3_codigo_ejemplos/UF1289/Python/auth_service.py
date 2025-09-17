# UF1289 - Diseño de componentes (Python)
from abc import ABC, abstractmethod

class AuthService(ABC):
    @abstractmethod
    def login(self, user: str, password: str) -> bool:
        pass

    @abstractmethod
    def logout(self, user: str) -> None:
        pass

class SimpleAuthService(AuthService):
    def login(self, user: str, password: str) -> bool:
        return user == "admin" and password == "1234"

    def logout(self, user: str) -> None:
        print(f"{user} logged out.")
