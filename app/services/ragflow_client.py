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

    async def list_datasets(self) -> dict:
        """Return datasets available to the configured RAGFlow user."""

        url = f"{self.base_url}/api/v1/datasets"

        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=self._headers(),
                timeout=30.0,
            )

        response.raise_for_status()
        return response.json()

    async def create_dataset(self, name: str) -> dict:
        """Create a dataset in RAGFlow."""

        url = f"{self.base_url}/api/v1/datasets"

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                headers=self._headers(),
                json={"name": name},
                timeout=30.0,
            )

        response.raise_for_status()
        return response.json()
