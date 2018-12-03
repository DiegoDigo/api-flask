from app_factory import create_app
from blueprints.usuarios.model import User

app = create_app()

if __name__ == '__main__':
    def create_user_default() -> None:
        print(User.find_by_email("di3g0d0ming05@gmail.com"))
        if not User.find_by_email("di3g0d0ming05@gmail.com"):
            User(username="Admin", email="di3g0d0ming05@gmail.com", password="123").save()
