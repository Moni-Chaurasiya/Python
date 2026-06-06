from sqlmodel import Relationship, SQLModel, Field, Column
from datetime import datetime, timezone
import uuid
from typing import Optional
import sqlalchemy.dialects.postgresql as pg
# from .models import Book
from src.auth import models

class Review(SQLModel,table=True):
    __tablename__="review"
    
    uid:uuid.UUID=Field(
        saa_column=Column(pg.UUID,nullable=False,primary_key=True,default=uuid.uuid4)
    )
    rating:int =Field(lt=5)
    review_text:str
    user_uid:Optional[uuid.UUID]=Field(default=None,foreign_key="users.uid")
    created_at:datetime=Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    updateded_at:datetime=Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    user:Optional["models.User"] = Relationship(back_populates="books")
    
def __rep__(self):
    return f"<Review for {self.book_uid} by user {self.user_uid}>"