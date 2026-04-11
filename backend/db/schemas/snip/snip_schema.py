from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base


class Snip(Base):
    __tablename__ = "snips"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
