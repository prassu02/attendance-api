import os
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

# ===== ENV CONFIG =====
SECRET_KEY = os.getenv("SECRET_KEY")
ALGO = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_HOURS = int(os.getenv("ACCESS_TOKEN_EXPIRE_HOURS", 24))

# Fail fast if missing (professional practice)
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in environment variables")

# ===== PASSWORD CONTEXT =====
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ===== PASSWORD FUNCTIONS =====
def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)


# ===== TOKEN FUNCTION =====
def create_token(data: dict):
    to_encode = data.copy()   # ✅ avoids mutation bug
    to_encode["exp"] = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGO)
