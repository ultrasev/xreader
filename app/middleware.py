import time
from fastapi import Request
from typing import Callable
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

# Define allowed origins
ALLOWED_ORIGINS = [
    "http://localhost:3000",     # Development environment
    "http://localhost:8000",     # Development environment
    "https://your-production-domain.com"  # Production domain
]

# Define allowed HTTP methods
ALLOWED_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

# Define allowed headers
ALLOWED_HEADERS = [
    "Content-Type",
    "Authorization",
    "X-Experimental-Stream-Data"
]

# CORS configuration
CORS_CONFIG = {
    "allow_origins": ALLOWED_ORIGINS,
    "allow_credentials": True,
    "allow_methods": ALLOWED_METHODS,
    "allow_headers": ALLOWED_HEADERS,
    "expose_headers": ["X-Experimental-Stream-Data"],
    "max_age": 600
}

async def log_requests(request: Request, call_next: Callable) -> Response:
    """Log request and response details with timing information

    Args:
        request: The incoming request
        call_next: The next middleware/route handler in the chain

    Returns:
        Response: The response from the next handler
    """
    start_time = time.time()
    logger.info(f"Request: {request.method} {request.url}")
    logger.info(f"Headers: {request.headers}")
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"Process time: {process_time:.3f}s")
    return response
