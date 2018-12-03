import jwt
import datetime


def encode_auth_token(user_name: str) -> str:
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow(),
            'sub': user_name
        }
        return jwt.encode(
            payload,
            ';+$.;Wfo#-yN',
            algorithm='HS256'
        )
    except Exception as e:
        return str(e)
