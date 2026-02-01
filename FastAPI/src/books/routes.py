from fastapi import APIRouter,status,HTTPException

from typing import List
from src.books.schemas import Book,UpdateBook
from src.books.book_data import books

book_router=APIRouter()

@book_router.get('/',response_model=List[Book])
async def get_all_books()-> list:
    return books

@book_router.get("/{id}",response_model=Book)
async def get_book_by_id(id:int):
    try:
    #  for book in books:
    #     if book["id"] ==id:
    #         return book
       return books[id]
    except IndexError:
        raise HTTPException(status_code=404,detail="Index out of range")

@book_router.post("/",response_model=List[Book],status_code=status.HTTP_200_OK)
async def create_book(book: Book) -> dict:
    books.append(book.dict())
    return books

@book_router.put("/{book_id}")
async def update_book(book_id: int, updated_book:Book) -> dict:
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books[index] = updated_book.dict()
            return {
                "message": "Book updated successfully",
                "book": books[index]
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )

@book_router.patch("/{book_id}")
async def update_book(book_id: int, updated_book:UpdateBook) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = updated_book.title
            book["publisher"]= updated_book.publisher
            book["author"]=updated_book.author
            book["page_count"]=updated_book.page_count
            book["language"]=updated_book.language
            return {
                "message": "Book updated successfully",
                "book": book
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


@book_router.delete('/{book_id}')
async def delete_book(book_id:int):
    try:
        # if book_id <0 or book_id >= len(books):
        #     raise HTTPException(status_code=404,detail="Index out of ranges")
        # del books[book_id]
        # return {"messgae":"Book has been deleted successfully","data":f"{books}"}
        # OR
        # for index,book in enumerate(books):
        #     if book["id"]==book_id:
        #         del books[index]
        #         return {"message":"Book has been deleted successfully"}
        # OR
        for book in books:
            if book["id"]==book_id:
                books.remove(book)
                return {"successfully deleted"}
            
        raise HTTPException(status_code=404,detail="Book not found")
    except:
        raise HTTPException(status_code=404,detail="Index out of range")