import jwt
import datetime

from blueprints.usuarios.model import User


def encode_auth_token(user: User) -> str:
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow(),
            'sub': user.username,
            'roles': [user.email]
        }
        return jwt.encode(
            payload,
            ';+$.;Wfo#-yN',
            algorithm='HS256'
        )
    except Exception as e:
        return str(e)
