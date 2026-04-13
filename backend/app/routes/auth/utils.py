from argon2 import PasswordHasher

ph = PasswordHasher()

def hash_password(password: str) -> str:
    if not password:
        raise ValueError("Password cannot be empty")
    return ph.hash(password)

def verify_password(hashed_password: str, password: str) -> bool:
    return ph.verify(hashed_password, password)
