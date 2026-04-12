from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.db.schemas.comment.comment_schema import Comment
from backend.db.schemas.user.user_schema import User
from db.db import Base


class Snip(Base):
    __tablename__ = "snips"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    code: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="snip")
    user: Mapped["User"] = relationship("User", back_populates="snips")
