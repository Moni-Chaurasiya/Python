from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.books.routes import book_router
from src.db.main import init_db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Server is starting...")
    try:
        await init_db()
    except Exception as e:
       logger.error(f"Database init failed: {e}")
       raise
    yield
    logger.info("Server has been stopped")

version = "v1"

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=version,
    lifespan=lifespan
)

@app.get("/")
async def health():
    return {"status": "server is running"}

app.include_router(
    book_router,
    prefix=f"/api/{version}/books",
    tags=["book"]
)
