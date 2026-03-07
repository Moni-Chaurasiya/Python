# This file defines Pydantic schemas for API request/response validation
# It handles data validation and serialization between client and server
# Unlike models.py (which talks to database), schemas.py talks to the client

# BaseModel: Pydantic base class for creating data validation models
# Used for: Request validation, Response formatting, Data serialization
from pydantic import BaseModel

# Import datetime for date/time fields in schemas
from datetime import datetime

# Import uuid for UUID fields
import uuid

# Book schema: Represents the complete book data structure
# Used for API responses (returning book data to clients)
# Inherits from BaseModel for automatic validation and JSON serialization
class Book(BaseModel):
    # uid: Unique identifier, matches the database model
    uid: uuid.UUID
    # title: Book title
    title: str
    # author: Book author
    author: str
    # publisher: Book publisher
    publisher: str
    # published_date: Publication date (stored as string)
    published_date: str
    # page_count: Number of pages
    page_count: int
    # language: Book language
    language: str
    # created_at: Creation timestamp
    created_at: datetime
    # updated_at: Last update timestamp
    updated_at: datetime

# BookCreateModel: Schema for creating new books
# Used for POST requests when clients want to add new books
# Only includes fields that clients should provide (excludes auto-generated fields like uid, timestamps)
class BookCreateModel(BaseModel):
    # title: Required field for book title
    title: str
    # author: Required field for book author
    author: str
    # publisher: Required field for book publisher
    publisher: str
    # This field represents the publication date
    published_date: str
    # page_count: Required field for number of pages
    page_count: int
    # language: Required field for book language
    language: str

# UpdateBook: Schema for updating existing books
# Used for PATCH/PUT requests to modify book data
# All fields are optional since updates might only change some fields
class UpdateBook(BaseModel):
    # title: Optional field for updating book title
    title: str
    # author: Optional field for updating book author
    author: str
    # publisher: Optional field for updating book publisher
    publisher: str
    # page_count: Optional field for updating page count
    page_count: int
    # language: Optional field for updating book language
    language: str