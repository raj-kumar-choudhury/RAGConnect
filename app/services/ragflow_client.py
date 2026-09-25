import httpx

from app.core.config import settings


class RAGFlowClient:
    """Client for communicating with the RAGFlow API."""

    def __init__(self) -> None:
        self.base_url = settings.ragflow_base_url.rstrip("/")
        self.api_key = settings.ragflow_api_key

    def _headers(self) -> dict[str, str]:
        headers = {
            "Content-Type": "application/json",
        }

        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        return headers
