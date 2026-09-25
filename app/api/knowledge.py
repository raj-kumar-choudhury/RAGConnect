from fastapi import APIRouter

from app.models.knowledge import (
    KnowledgeDocumentRequest,
    KnowledgeDocumentResponse,
)
from app.providers.factory import get_provider


router = APIRouter(prefix="/api/v1/knowledge", tags=["knowledge"])


@router.post("/documents", response_model=KnowledgeDocumentResponse)
async def ingest_document(
    request: KnowledgeDocumentRequest,
) -> KnowledgeDocumentResponse:
    """Ingest a knowledge document through the configured RAG provider."""

    provider = get_provider()

    result = await provider.ingest(
        name=request.name,
        content=request.content,
        metadata=request.metadata,
    )

    return KnowledgeDocumentResponse(
        document_id=result["document_id"],
        name=request.name,
        status=result["status"],
        metadata=request.metadata,
    )