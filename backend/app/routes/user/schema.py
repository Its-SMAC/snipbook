from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str | None = None

class UserInDB(User):
    hashed_password: str
