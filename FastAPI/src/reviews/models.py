from sqlmodel import SQLModel, Field, Relationship, Column
from datetime import datetime
import uuid
from typing import Optional, TYPE_CHECKING
import sqlalchemy.dialects.postgresql as pg

if TYPE_CHECKING:
    from src.auth.models import User
    from src.books.models import Book


class Review(SQLModel, table=True):
    __tablename__ = "review"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            nullable=False,
            default=uuid.uuid4
        )
    )

    rating: int = Field(le=5)
    review_text: str

    user_uid: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="users.uid"
    )

    book_uid: Optional[uuid.UUID] = Field(
        default=None,
        foreign_key="books.uid"
    )

    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.utcnow
        )
    )

    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.utcnow
        )
    )

    user: Optional["User"] = Relationship(
        back_populates="reviews"
    )

    book: Optional["Book"] = Relationship(
        back_populates="reviews"
    )

    def __repr__(self):
        return f"<Review for {self.book_uid} by user {self.user_uid}>"