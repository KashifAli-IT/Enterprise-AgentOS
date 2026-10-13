from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.routes.health import router as health_router
from app.core.config import get_settings
from app.core.errors import (
    http_exception_handler,
    unhandled_exception_handler,
    validation_exception_handler,
)

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="A controlled platform for secure, observable AI agent workflows.",
    version="0.1.0",
)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

app.include_router(health_router, prefix=settings.api_v1_prefix)


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    """Provide basic API information."""
    return {
        "name": settings.app_name,
        "status": "running",
        "docs": "/docs",
    }
