from app.providers.base import RAGProvider
from app.providers.ragflow.provider import RAGFlowProvider


def get_provider() -> RAGProvider:
    """Return the configured RAG provider."""

    return RAGFlowProvider()