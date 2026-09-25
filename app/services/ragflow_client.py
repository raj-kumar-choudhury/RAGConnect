from pathlib import Path

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

    def _auth_headers(self) -> dict[str, str]:
        headers = {}

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

    async def upload_document(
        self,
        dataset_id: str,
        file_path: str | Path,
    ) -> dict:
        """Upload a document to a RAGFlow dataset."""

        path = Path(file_path)

        if not path.is_file():
            raise FileNotFoundError(f"Document not found: {path}")

        url = f"{self.base_url}/api/v1/datasets/{dataset_id}/documents"

        with path.open("rb") as document:
            files = {
                "file": (path.name, document),
            }
            data = {
                "display_name": path.name,
            }

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url,
                    headers=self._auth_headers(),
                    files=files,
                    data=data,
                    timeout=60.0,
                )

        response.raise_for_status()
        return response.json()

    async def list_documents(self, dataset_id: str) -> dict:
        """Return documents and their current processing status."""

        url = f"{self.base_url}/api/v1/datasets/{dataset_id}/documents"

        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=self._headers(),
                timeout=30.0,
            )

        response.raise_for_status()
        return response.json()

    async def parse_documents(
        self,
        dataset_id: str,
        document_ids: list[str],
    ) -> dict:
        """Start parsing/chunking for documents in a RAGFlow dataset."""

        if not document_ids:
            raise ValueError("At least one document ID is required")

        url = f"{self.base_url}/api/v1/datasets/{dataset_id}/chunks"

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                headers=self._headers(),
                json={"document_ids": document_ids},
                timeout=30.0,
            )

        response.raise_for_status()
        return response.json()
