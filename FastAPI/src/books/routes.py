from fastapi import APIRouter,status,HTTPException, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from src.books.service import BookService
from src.books.schemas import Book,UpdateBook
# from src.books.book_data import books
from src.db.main import get_session

book_router=APIRouter()
book_service=BookService()
@book_router.get('/',response_model=List[Book])
async def get_all_books(session:AsyncSession=Depends(get_session))-> list:
    books=await book_service.get_all_book(session)
    return books

@book_router.get("/{book_uid}",response_model=Book)
async def get_book_by_id(book_uid:str, session:AsyncSession=Depends(get_session)):
    try:
    #  for book in books:
    #     if book["id"] ==id:
    #         return book
       book = await book_service.get_book(book_uid,session)
       return book
    except IndexError:
        raise HTTPException(status_code=404,detail="Index out of range")

@book_router.post("/",response_model=Book,status_code=status.HTTP_200_OK)
async def create_book(book: Book,session:AsyncSession=Depends(get_session)) -> dict:
    # new_book= book_data.model_dump()
    # books.append(book.dict())
    new_book =await book_service.create_book(book,session)
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


@book_router.patch("/{book_uid}")
async def update_book(book_uid: str, updated_book: UpdateBook, session: AsyncSession = Depends(get_session)):
    
    book = await book_service.update_book(book_uid, updated_book, session)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

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

@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session)):

    book = await book_service.delete_book(book_uid, session)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

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