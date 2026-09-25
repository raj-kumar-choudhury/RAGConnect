from fastapi import APIRouter

from app.models.query import QueryRequest
from app.models.response import RAGResponse
from app.providers.factory import get_provider


router = APIRouter(prefix="/api/v1", tags=["query"])


@router.post("/query", response_model=RAGResponse)
async def query(request: QueryRequest) -> RAGResponse:
    """Query the configured RAG provider."""

    provider = get_provider()

    return await provider.query(
        question=request.question,
    )
