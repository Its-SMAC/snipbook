from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    snip_id: Mapped[int] = mapped_column(ForeignKey("snips.id"))
