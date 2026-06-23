import uuid
from datetime import date, datetime
from typing import TYPE_CHECKING, List, Optional

import sqlalchemy.dialects.postgresql as pg
from sqlmodel import Column, Field, Relationship, SQLModel

if TYPE_CHECKING:
    from src.books.models import Book
    


class BookTag(SQLModel,table=True):
    __tablename__ = "book_tags"
    book_id:uuid.UUID= Field(default= None,foreign_key="books.uid", primary_key=True)
    tag_id:uuid.UUID = Field(default=None, foreign_key="tags.uid", primary_key=True)
    
class Tag(SQLModel, table=True):
    __tablename__="tags"
    uid:uuid.UUID =Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
        
    )
    name:str = Field(sa_column=Column(pg.VARCHAR,nullable=False))
    created_at:datetime=Field(sa_column=Column(pg.TIMESTAMP,default=datetime.utcnow))
    books:List["Book"]=Relationship(
        link_model=BookTag,
        back_populates="tags",
        sa_relationship_kwargs={"lazy":"selectin"},
    )
    
    def __repr__(self) -> str:
        return f"<Tag {self.name}>"