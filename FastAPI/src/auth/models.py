from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Relationship, SQLModel, Field, Column
import uuid
from datetime import datetime, timezone
import sqlalchemy.dialects.postgresql as pg

if TYPE_CHECKING:
    from src.books.models import Book
    from src.reviews.models import Review


class User(SQLModel, table=True):

    __tablename__ = "users"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID(as_uuid=True),
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )

    username: str
    email: str
    first_name: str
    last_name: str
    role:str=Field(sa_column=Column(pg.VARCHAR,nullable=False, server_default="user"))
    password_hash:str= Field(exclude=True)
    is_verified: bool = False

    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),
            default=lambda: datetime.now(timezone.utc)
        )
    )

    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),
            default=lambda: datetime.now(timezone.utc)
        )
    )
    books: List["Book"] = Relationship(back_populates="user", sa_relationship_kwargs={'lazy': "selectin"})
    reviews: List["Review"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"lazy": "selectin"}
    )
    def __repr__(self):
        return f"<User {self.username}>"