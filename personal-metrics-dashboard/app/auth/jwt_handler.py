#Crea  y valida tokens JWT(JSON WEB TOKENS)

import jwt

SECRET_KEY = "password123"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: int = 3600) -> str:
    to_encode = data.copy()
    to_encode.update({"exp": expires_delta})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_jwt
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None