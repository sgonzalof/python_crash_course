# UF1290 - Implementación e integración (Python)
class UserComponent:
    def __init__(self, username: str):
        self.username = username

class UserService:
    def register(self, user: UserComponent):
        print(f"User registered: {user.username}")

if __name__ == "__main__":
    user = UserComponent("alice")
    service = UserService()
    service.register(user)
