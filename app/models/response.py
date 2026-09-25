from pydantic import BaseModel, Field


class RAGSource(BaseModel):
    document: str
    similarity: float | None = None
    vector_similarity: float | None = None
    term_similarity: float | None = None


class RAGResponse(BaseModel):
    answer: str
    sources: list[RAGSource] = Field(default_factory=list)
    session_id: str | None = None
