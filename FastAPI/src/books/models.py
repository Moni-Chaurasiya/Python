# This file defines the database models/tables for the application
# It talks directly to the database (PostgreSQL or any SQL database)

# Import SQLModel components:
# SQLModel: Base class that combines SQLAlchemy ORM with Pydantic validation
# Field: Defines column properties like primary key, default values, etc.
# Column: Direct SQLAlchemy column customization for advanced options
from sqlmodel import SQLModel, Field, Column

# Import PostgreSQL-specific data types from SQLAlchemy
# pg: Provides PostgreSQL types like UUID, TIMESTAMP for better type safety
import sqlalchemy.dialects.postgresql as pg

# Import datetime classes for timestamp fields
# datetime: For date/time handling
# timezone: For UTC timezone support
from datetime import datetime, timezone

# Import uuid module for generating unique identifiers
# uuid: Standard library for UUID generation and handling
import uuid

# Define the Book model as a database table
# SQLModel: Inherits from SQLModel for ORM capabilities
# table=True: Tells SQLModel to create this as an actual database table
class Book(SQLModel, table=True):
    # __tablename__: Explicitly set the table name in the database
    __tablename__ = "books"

    # uid: Unique identifier for each book, using UUID
    # Field: Defines this as a database column with specific properties
    # sa_column: Uses SQLAlchemy Column for advanced configuration
    # pg.UUID: PostgreSQL UUID type for database-level UUID support
    # nullable=False: This field cannot be NULL
    # primary_key=True: This is the primary key of the table
    # default=uuid.uuid4: Automatically generates a UUID v4 when creating new records
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )

    # title: Book title as a string
    # No additional constraints, so it uses default string type
    title: str

    # author: Book author as a string
    author: str

    # publisher: Book publisher as a string
    publisher: str

    # published_date: Publication date stored as string (could be improved to date type)
    published_date: str

    # page_count: Number of pages as integer
    page_count: int

    # language: Book language as string
    language: str

    # created_at: Timestamp when the record was created
    # Field with sa_column for PostgreSQL TIMESTAMP type
    # default: Lambda function that returns current UTC time when record is created
    # created_at: Timestamp when the record was created
    # Use TIMESTAMP WITH TIME ZONE so we can store aware datetimes directly
    # default: Lambda returns a UTC-aware datetime object
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP(timezone=True), default=lambda: datetime.now(timezone.utc))
    )

    # updated_at: Timestamp when the record was last updated
    # Same configuration as created_at (timezone-aware)
    updated_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP(timezone=True), default=lambda: datetime.now(timezone.utc))
    )

    # __repr__: String representation method for debugging
    # Returns a readable string showing the book title
    def __repr__(self):
        return f"<Book {self.title} >"
    
    
# [
#     "adding users",
#     "change roles",
#     "crud on users",
#     "book submission",
#     "crud on reviews",
#     "revoking access",
# ]

# ["crud on their own book submission","crud on their reviews", "crud on their own account"]