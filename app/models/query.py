from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1)


class QuerySource(BaseModel):
    document: str
    similarity: float | None = None
    vector_similarity: float | None = None
    term_similarity: float | None = None


class QueryResponse(BaseModel):
    answer: str
    sources: list[QuerySource] = Field(default_factory=list)
