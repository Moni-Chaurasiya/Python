# This file initializes the FastAPI application
# It sets up the main app, includes routers, and handles startup/shutdown events

# Import FastAPI for creating the web application
from fastapi import FastAPI

# Import asynccontextmanager for managing app lifespan
# This allows running code on startup and shutdown
from contextlib import asynccontextmanager

# Import the book router to include book-related endpoints
from src.books.routes import book_router

# Import database initialization function
from src.db.main import init_db
from src.auth.routes import auth_router
# Import logging for application logging
import logging

# Configure logging to show info level messages
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the lifespan context manager for app startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Log that server is starting
    logger.info("Server is starting...")
    try:
        # Initialize the database (create tables)
        await init_db()
    except Exception as e:
        # Log any database initialization errors
       logger.error(f"Database init failed: {e}")
       raise
    # Yield control to the app (app runs here)
    yield
    # Shutdown: Log that server has stopped
    logger.info("Server has been stopped")

# Set API version for URL paths
version = "v1"

# Create the FastAPI application instance
app = FastAPI(
    # Application title
    title="Bookly",
    # Application description
    description="A REST API for a book review web service",
    # API version
    version=version,
    # Lifespan handler for startup/shutdown
    # lifespan=lifespan
)

# Health check endpoint
@app.get("/")
async def health():
    return {"status": "server is running"}

# Include the book router with a prefix
# prefix: All book routes will be under /api/v1/books
# tags: Groups endpoints in documentation
app.include_router(
    book_router,
    prefix=f"/api/{version}/books",
    tags=["book"]
)
app.include_router(
    auth_router,
    prefix=f"/api/{version}/auth",
    tags=["auth"]
)
