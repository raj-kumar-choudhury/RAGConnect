from fastapi import APIRouter

from app.models.query import QueryRequest, QueryResponse, QuerySource
from app.providers.factory import get_provider


router = APIRouter(prefix="/api/v1", tags=["query"])


@router.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest) -> QueryResponse:
    """Query the configured RAG provider."""

    provider = get_provider()

    result = await provider.query(
        question=request.question,
    )

    data = result.get("result", {}).get("data") or {}
    answer = data.get("answer", "")
    reference = data.get("reference") or {}

    sources = [
        QuerySource(
            document=chunk.get("document_name", ""),
            similarity=chunk.get("similarity"),
            vector_similarity=chunk.get("vector_similarity"),
            term_similarity=chunk.get("term_similarity"),
        )
        for chunk in reference.get("chunks", [])
        if chunk.get("document_name")
    ]

    return QueryResponse(
        answer=answer,
        sources=sources,
    )