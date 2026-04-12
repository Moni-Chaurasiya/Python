# This file defines the API endpoints (routes) for the book management system
# It connects the client requests to the business logic in the service layer
# Routes handle HTTP requests and responses

# Import FastAPI components for building API endpoints
# APIRouter: Creates modular route handlers
# status: HTTP status codes
# HTTPException: For error responses
# Depends: Dependency injection for database sessions
from fastapi import APIRouter, status, HTTPException, Depends

# Import AsyncSession for database operations
from sqlmodel.ext.asyncio.session import AsyncSession

# Import List for type hints (list of books)
from typing import List

# Import BookService for business logic operations
from src.books.service import BookService

# Import schemas for request/response validation
from src.books.schemas import Book, UpdateBook, BookCreateModel

# Import commented out: Static book data (replaced by database)
# from src.books.book_data import books

# Import get_session dependency for database connections
from src.db.main import get_session
from typing import List
from src.auth.dependencies import AccessTokenBearer, RoleChecker
# Create an APIRouter instance for book-related endpoints
# This allows modular routing
book_router = APIRouter()

# Instantiate the BookService
# This provides access to all book operations
book_service = BookService()
access_token_bearer = AccessTokenBearer()
role_checker= Depends(RoleChecker(['admin','user']))

# GET endpoint to retrieve all books
# @book_router.get('/'): Defines GET route at root path
# response_model=List[Book]: Response will be a list of Book objects
# session=Depends(get_session): Injects database session
# -> list: Return type hint
@book_router.get('/', response_model=List[Book],dependencies= [role_checker])
async def get_all_books(session: AsyncSession = Depends(get_session),user_details=Depends(access_token_bearer), ) -> list:
    # Call service to get all books from database
    books = await book_service.get_all_book(session)
    # Return the list of books
    return books

# GET endpoint to retrieve a single book by UID
# {book_uid}: Path parameter for book identifier
# response_model=Book: Response will be a single Book object
@book_router.get("/{book_uid}", response_model=Book,dependencies= [role_checker])
async def get_book_by_id(book_uid: str, session: AsyncSession = Depends(get_session),user_details=Depends(access_token_bearer)):
    # Try-catch for error handling
    try:
        # Commented out: Old implementation using static data
        # for book in books:
        #     if book["id"] ==id:
        #         return book
        # Call service to get book by UID
        book = await book_service.get_book(book_uid, session)
        # Return the book
        return book
    # Handle index errors (though not applicable with database)
    except IndexError:
        raise HTTPException(status_code=404, detail="Index out of range")

# POST endpoint to create a new book
# response_model=Book: Response will be the created Book object
# status_code=status.HTTP_200_OK: Override default 201 for creation
# book: Book: Request body parameter (should be BookCreateModel for creation)
@book_router.post("/", response_model=Book, status_code=status.HTTP_200_OK, dependencies= [role_checker])
async def create_book(book: BookCreateModel, session: AsyncSession = Depends(get_session),user_details=Depends(access_token_bearer)) -> dict:
    # Commented out: Old implementation with static data
    # new_book= book_data.model_dump()
    # books.append(book.dict())
    # Call service to create new book
    new_book = await book_service.create_book(book, session)
    # Return the created book
    return new_book

# @book_router.put("/{book_id}")
# async def update_book(book_id: int, updated_book:Book) -> dict:
#     for index, book in enumerate(books):
#         if book["id"] == book_id:
#             books[index] = updated_book.dict()
#             return {
#                 "message": "Book updated successfully",
#                 "book": books[index]
#             }

#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Book not found"
#     )


# PATCH endpoint to update an existing book
# {book_uid}: Path parameter for book to update
# updated_book: Request body with fields to update
@book_router.patch("/{book_uid}",response_model=Book, dependencies= [role_checker])
async def update_book(book_uid: str, updated_book: UpdateBook, session: AsyncSession = Depends(get_session),user_details=Depends(access_token_bearer)):
    # Call service to update the book
    book = await book_service.update_book(book_uid, updated_book, session)
    # If book not found, raise 404 error
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    # Return the updated book
    return book



# @book_router.patch("/{book_uid}")
# async def update_book(book_uid: str, updated_book:UpdateBook,session:AsyncSession=Depends(get_session)) -> dict:
#     try:
        
#        updated_book= await book_service.update_book(book_uid, updated_book,session)
#        return updated_book
#     # for book in books:
#     #     if book["id"] == book_uid:
#     #         book["title"] = updated_book.title
#     #         book["publisher"]= updated_book.publisher
#     #         book["author"]=updated_book.author
#     #         book["page_count"]=updated_book.page_count
#     #         book["language"]=updated_book.language
#     #         return {
#     #             "message": "Book updated successfully",
#     #             "book": book
#     #         }
#     except:
        
#         raise HTTPException(
#           status_code=status.HTTP_404_NOT_FOUND,
#           detail="Book not found"
#         )

# DELETE endpoint to remove a book
# status_code=status.HTTP_204_NO_CONTENT: Returns 204 (no content) on success
@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT, dependencies= [role_checker])
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session),user_details=Depends(access_token_bearer)):
    # Call service to delete the book
    book = await book_service.delete_book(book_uid, session)
    # If book not found, raise 404 error
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    # Return None (204 No Content)
    return None

# @book_router.delete('/{book_uid}',status_code=status.HTTP_204_NO_CONTENT)
# async def delete_book(self,book_uid:str,session:AsyncSession=Depends(get_session)):
#     try:
#         # if book_id <0 or book_id >= len(books):
#         #     raise HTTPException(status_code=404,detail="Index out of ranges")
#         # del books[book_id]
#         # return {"messgae":"Book has been deleted successfully","data":f"{books}"}
#         # OR
#         # for index,book in enumerate(books):
#         #     if book["id"]==book_id:
#         #         del books[index]
#         #         return {"message":"Book has been deleted successfully"}
#         # OR
        
#         book = await book_service.delete_book(book_uid,session)
#         if book:
#             return None
#         else:
#             raise HTTPException(status_code=404,detail="Book not found")
#         # for book in books:
#         #     if book["id"]==book_id:
#         #         books.remove(book)
#         #         return {"successfully deleted"}
            
#     except:
#         raise HTTPException(status_code=404,detail="Index out of range")