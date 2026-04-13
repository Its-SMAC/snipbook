from fastapi import APIRouter

from backend.app.routes.user.schema import User
from backend.db.db import get_db

from .schema import Token

VERSION="v1"
router = APIRouter(prefix=f"/auth{VERSION}", tags=["auth"])


router.post("/login")
async def login(user: User) -> Token:
    if not user:
        raise ValueError("User cannot be empty")
    db = get_db
    return Token(access_token="")
