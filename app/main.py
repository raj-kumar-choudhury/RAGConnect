from fastapi import FastAPI

from app.api.query import router as query_router
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    description="RAG API layer for integrating applications with RAGFlow",
    version=settings.app_version,
)


app.include_router(query_router)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.app_version,
    }
