from pydantic import BaseModel
from datetime import datetime
import uuid
class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at:datetime
    updated_at:datetime
    
class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    publish_data:datetime
    page_count: int
    language: str
class UpdateBook(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str