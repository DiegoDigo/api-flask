from sqlalchemy.exc import IntegrityError

from blueprints.usuarios.model import User
from utilitary.token import encode_auth_token


def create_user_default() -> tuple:
    try:
        User(username='admin', email="di3g0d0ming05@gmail.com", password="123").save()
        return dict(message="create at"), 200
    except IntegrityError:
        return dict(message="User already exists!"), 409


def login(user_data: dict) -> tuple:
    user = User.find_by_email(user_data.get('email', None))
    if user and user.password_is_valid(user_data.get('password', None)):
        return dict(token=encode_auth_token(user.username).decode("UTF-8")), 200
    return dict(message="user or password not exist"), 403
