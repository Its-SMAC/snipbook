from typing import Text

from pydantic import BaseModel


class SnipBase(BaseModel):
    title: str
    language: str
    description: str | None = None
    code: Text

class SnipCreate(SnipBase):
    pass

class SnipInDB(SnipBase):
    id: int

class SnipResponse(SnipBase):
    id:int
    
    class Config:
        orm_mode = True

class SnipUpdate(BaseModel):
    title: str | None = None
    language: str | None = None
    description: str | None = None
    code: Text | None = None
