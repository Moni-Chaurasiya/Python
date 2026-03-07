# This file contains the business logic layer
# It handles all database operations and data processing
# Acts as an intermediary between routes (API endpoints) and models (database)

# Import AsyncSession for asynchronous database operations
from sqlmodel.ext.asyncio.session import AsyncSession

# Import schemas for data validation and type hints
from .schemas import BookCreateModel
from .schemas import UpdateBook

# Import select and desc for building database queries
# select: Creates SELECT queries
# desc: Orders results in descending order
from sqlmodel import select, desc

# Import the Book model for database operations
from .models import Book

# Import datetime for date handling (commented out in original)
# from datetime import datetime

# Import datetime for handling publication dates
from datetime import datetime

# BookService class: Contains all business logic for book operations
# This is a service layer that encapsulates database operations
class BookService:

    # Method to get all books from database
    # async: Asynchronous function for non-blocking database operations
    # session: Database session dependency injected from routes
    async def get_all_book(self, session: AsyncSession):
        # Create a SELECT query for all Book records
        # order_by(desc(Book.created_at)): Order by creation date, newest first
        statement = select(Book).order_by(desc(Book.created_at))
        # Execute the query asynchronously
        result = await session.exec(statement)
        # Return all results as a list
        return result.all()

    # Method to get a single book by its UID
    # book_uid: String representation of the book's UUID
    # session: Database session
    async def get_book(self, book_uid: str, session: AsyncSession):
        # Create a SELECT query filtered by UID
        # where(Book.uid == book_uid): Filter condition
        statement = select(Book).where(Book.uid == book_uid)
        # Execute the query
        result = await session.exec(statement)
        # Get the first result (should be only one due to unique UID)
        book = result.first()
        # Return the book if found, otherwise None
        return book if book is not None else None

    # Commented out: Alternative implementation of create_book
    # This version manually handled date parsing
    # async def create_book(self,book_data:BookCreateModel,session:AsyncSession):
    #     book_data_dict= book_data.model_dump()
    #     new_book=Book(**book_data_dict)
    #     new_book.published_date=datetime.strptime(book_data_dict['published_date'],"%Y-%m-%d")
    #     session.add(new_book)
    #     await session.commit()
    #     return new_book

    # Method to create a new book
    # book_data: Validated data from the API request
    # session: Database session
    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        # Convert Pydantic model to dictionary
        # model_dump(): Serializes the model to a dict
        book_data_dict = book_data.model_dump()
        # Create a new Book instance using dictionary unpacking
        # **book_data_dict: Unpacks dict as keyword arguments
        new_book = Book(**book_data_dict)
        # Add the new book to the session (stages for insertion)
        session.add(new_book)
        # Commit the transaction to save to database
        await session.commit()
        # Return the created book (now has database-generated fields like uid)
        return new_book

    # Method to update an existing book
    # book_uid: ID of the book to update
    # update_data: Fields to update
    # session: Database session
    async def update_book(self, book_uid: str, update_data: UpdateBook, session: AsyncSession):
        # First, get the existing book
        book_to_update = await self.get_book(book_uid, session)
        # Check if the book exists
        if book_to_update is not None:
            # Convert update data to dictionary
            update_data_dict = update_data.model_dump()
            # Iterate through update fields and set them on the book
            # setattr: Dynamically sets attributes on the object
            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)
            # Commit the changes to database
            await session.commit()
            # Return the updated book
            return book_to_update

    # Method to delete a book
    # book_uid: ID of the book to delete
    # session: Database session
    async def delete_book(self, book_uid: str, session: AsyncSession):
        # Get the book to delete
        book_to_delete = await self.get_book(book_uid, session)

        # If book doesn't exist, return None
        if book_to_delete is None:
            return None

        # Delete the book from the session
        await session.delete(book_to_delete)
        # Commit the deletion
        await session.commit()
        # Return the deleted book (for confirmation)
        return book_to_delete

