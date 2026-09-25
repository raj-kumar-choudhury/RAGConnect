from fastapi import FastAPI

app = FastAPI(
    title="RAGConnect",
    description="RAG API layer for integrating applications with RAGFlow",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "RAGConnect",
        "version": "0.1.0",
    }