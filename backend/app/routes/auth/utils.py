import os
from datetime import datetime, timedelta

from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError, VerifyMismatchError
from jose import jwt

from backend.app.routes.user.schema import UserInDB

ph = PasswordHasher()

SECRET_KEY = os.environ["JWT_SECRET"]  # guarda no .env, nunca no código
ALGORITHM = "HS256"
ACCESS_EXPIRE_MIN = 15

def hash_password(password: str) -> str:
    if not password:
        raise ValueError("Password cannot be empty")
    return ph.hash(password)

def verify_password(hashed_password: str, password: str) -> bool:
    try:
        return ph.verify(hashed_password, password)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        return False

def create_access_token(username: str) -> str:
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_EXPIRE_MIN)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def get_user(db, name: str):
    if name in db:
        return UserInDB(**db[name])
    return None
