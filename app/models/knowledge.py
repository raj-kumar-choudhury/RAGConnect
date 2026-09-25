from pydantic import BaseModel, Field


class KnowledgeDocumentRequest(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    dataset_id: str = Field(..., min_length=1)


class KnowledgeDocumentResponse(BaseModel):
    dataset_id: str
    document_id: str
    title: str
    status: str
