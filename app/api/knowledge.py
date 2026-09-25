from fastapi import APIRouter

from app.core.config import settings
from app.models.knowledge import (
    KnowledgeDocumentRequest,
    KnowledgeDocumentResponse,
)
from app.services.ragflow_client import RAGFlowClient


router = APIRouter(prefix="/api/v1/knowledge", tags=["knowledge"])


@router.post("/documents", response_model=KnowledgeDocumentResponse)
async def ingest_document(
    request: KnowledgeDocumentRequest,
) -> KnowledgeDocumentResponse:
    """Upload SkillFlow lesson text to RAGFlow and start parsing."""

    client = RAGFlowClient()

    upload_result = await client.upload_text_document(
        dataset_id=request.dataset_id,
        title=request.title,
        content=request.content,
    )

    documents = upload_result.get("data") or []
    if not isinstance(documents, list) or not documents:
        raise ValueError("RAGFlow did not return an uploaded document")

    document_id = documents[0].get("id")
    if not document_id:
        raise ValueError("RAGFlow did not return a document ID")

    await client.parse_documents(
        dataset_id=request.dataset_id,
        document_ids=[document_id],
    )

    return KnowledgeDocumentResponse(
        dataset_id=request.dataset_id,
        document_id=document_id,
        title=request.title,
        status="processing",
    )
