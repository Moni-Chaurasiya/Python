# Import necessary modules for database operations
# SQLModel: Provides ORM capabilities combining SQLAlchemy and Pydantic for database models
# create_engine: Creates a database engine for synchronous/asynchronous connections
# text: Allows execution of raw SQL queries
# SQLModel: Base class for database models
from sqlmodel import create_engine, text, SQLModel

# AsyncEngine: For asynchronous database operations
from sqlalchemy.ext.asyncio import AsyncEngine

# Config: Custom configuration class to load database URL from environment
from src.config import Config

# AsyncSession: Asynchronous database session for ORM operations
from sqlmodel.ext.asyncio.session import AsyncSession

# sessionmaker: Factory for creating database sessions
from sqlalchemy.orm import sessionmaker

# Duplicate import - should be removed, but keeping for now
from src.config import Config

# Create an asynchronous database engine
# AsyncEngine: Wraps the synchronous engine for async operations
async_engine = AsyncEngine(
    # create_engine: Initializes the database connection
    create_engine(
        # url: Database connection string from config (e.g., postgresql://user:pass@host/db)
        url=Config.DATABASE_URL,
        # echo: Logs all SQL statements executed (useful for debugging)
        echo=True,
        # connect_args: Additional connection parameters (SSL disabled here)
        # connect_args={"ssl": False}
    )
)

# Asynchronous function to initialize the database
# This creates all tables defined in the models
async def init_db():
    # async with: Context manager for async database connection
    async with async_engine.begin() as conn:
        # Import the Book model here to ensure it's registered with SQLModel
        from src.books.models import Book

        # Create all tables defined in SQLModel metadata
        # This executes CREATE TABLE statements for all models
        await conn.run_sync(SQLModel.metadata.create_all)

        # Commented out: Example of executing raw SQL query
        # statement = text("SELECT 'hello';")
        # result = await conn.execute(statement)
        # print(result.all())

# Dependency function to provide database sessions to routes
# Returns AsyncSession: The type hint indicates it yields an AsyncSession
async def get_session() -> AsyncSession: # type: ignore
    # Create a session factory configured for async operations
    Session = sessionmaker(
        # bind: Connect the session to our async engine
        bind=async_engine,
        # class_: Specify AsyncSession for async operations
        class_=AsyncSession,
        # expire_on_commit: Keep objects accessible after commit (prevents lazy loading issues)
        expire_on_commit=False
    )

    # async with: Context manager that automatically handles session lifecycle
    async with Session() as session:
        # yield: Makes this a dependency that provides the session and cleans up after
        yield session

# Commented out: Alternative synchronous engine setup (not used)
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
