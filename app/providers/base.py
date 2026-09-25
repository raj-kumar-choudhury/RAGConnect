from abc import ABC, abstractmethod
from typing import Any

from app.models.response import RAGResponse


class RAGProvider(ABC):
    """Abstract interface for RAG providers."""

    @abstractmethod
    async def ingest(
        self,
        name: str,
        content: str,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Ingest knowledge into the provider."""
        raise NotImplementedError

    @abstractmethod
    async def query(
        self,
        question: str,
        session_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> RAGResponse:
        """Query the provider."""
        raise NotImplementedError