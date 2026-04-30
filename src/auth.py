from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secret"
ALGORITHM = "HS256"

def create_token(data: dict, hours: int = 24):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=hours)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)