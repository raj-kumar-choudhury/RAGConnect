from app.core.config import settings
from app.providers.base import RAGProvider
from app.providers.ragflow.provider import RAGFlowProvider


def get_provider() -> RAGProvider:
    """Return the configured RAG provider."""

    if settings.rag_provider.lower() == "ragflow":
        return RAGFlowProvider()

    raise ValueError(
        f"Unsupported RAG provider: {settings.rag_provider}"
    )