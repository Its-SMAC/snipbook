from fastapi import APIRouter, Depends, HTTPException, status

from backend.app.routes.auth.schema import LoginRequest
from backend.app.db.db import get_db

from .utils import get_user, verify_password

VERSION="v1"
router = APIRouter(prefix=f"/auth{VERSION}", tags=["auth"])


@router.post("/login")
async def login(body: LoginRequest, db=Depends(get_db)):
    user = get_user(db, body.name)
    if not user or not verify_password(hashed_password=user.hashed_password, password=body.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
