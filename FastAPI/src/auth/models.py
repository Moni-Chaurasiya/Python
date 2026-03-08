from sqlmodel import SQLModel, Field, Column
import uuid
from datetime import datetime, timezone
import sqlalchemy.dialects.postgresql as pg


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

    def __repr__(self):
        return f"<User {self.username}>"