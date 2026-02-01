from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config

engine= AsyncEngine(
    create_engine(
    url=Config.DATABASE_URL,
    echo=True,
   # connect_args={"ssl": False}
))

async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book
        
        await conn.run_sync(SQLModel.metadata.create_all)
        
        # statement =  text("SELECT 'hello';")
        
        # result =await conn.execute(statement)
        
        # print(result.all())


# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy import text
# from src.config import Config

# engine = create_async_engine(
#     Config.DATABASE_URL,
#     echo=True,
#     connect_args={"ssl": False}
# )

# async def init_db():
#     async with engine.begin() as conn:
#         result = await conn.execute(text("SELECT 'hello';"))
#         print(result.all())


# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy import text
# from src.config import Config

# engine = None

# def get_engine():
#     global engine
#     if engine is None:
#         engine = create_async_engine(
#             Config.DATABASE_URL,
#             echo=True,
#             connect_args={"ssl": False}
#         )
#     return engine

# async def init_db():
#     engine = get_engine()
#     async with engine.begin() as conn:
#         result = await conn.execute(text("SELECT 'hello';"))
#         print(result.all())
