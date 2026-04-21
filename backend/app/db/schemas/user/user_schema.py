from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.db.schemas.comment.comment_schema import Comment
from backend.app.db.schemas.snip.snip_schema import Snip
from backend.app.db.db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="user")
    snips: Mapped[list["Snip"]] = relationship("Snip", back_populates="user")
