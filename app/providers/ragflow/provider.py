from typing import Any

from app.core.config import settings
from app.providers.base import RAGProvider
from app.services.ragflow_client import RAGFlowClient


class RAGFlowProvider(RAGProvider):
    """RAGFlow implementation of the generic RAG provider interface."""

    def __init__(self) -> None:
        self.client = RAGFlowClient()
        self.dataset_id = settings.ragflow_dataset_id

    async def ingest(
        self,
        name: str,
        content: str,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Ingest knowledge into RAGFlow."""

        if not self.dataset_id:
            raise ValueError("RAGFLOW_DATASET_ID is not configured")

        upload_result = await self.client.upload_text_document(
            dataset_id=self.dataset_id,
            title=name,
            content=content,
        )

        documents = upload_result.get("data") or []

        if not isinstance(documents, list) or not documents:
            raise ValueError("RAGFlow did not return an uploaded document")

        document_id = documents[0].get("id")

        if not document_id:
            raise ValueError("RAGFlow did not return a document ID")

        await self.client.parse_documents(
            dataset_id=self.dataset_id,
            document_ids=[document_id],
        )

        return {
            "provider": "ragflow",
            "document_id": document_id,
            "status": "processing",
            "metadata": metadata or {},
        }

    async def query(
        self,
        question: str,
        session_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Query RAGFlow."""

        result = await self.client.chat(
            question=question,
            session_id=session_id,
        )

        return {
            "provider": "ragflow",
            "result": result,
            "metadata": metadata or {},
        }