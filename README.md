# RAGConnect

RAGConnect is an independent RAG API layer that will connect SkillFlow with RAGFlow.

## Current Architecture

```text
React
  ↓
SkillFlow Node.js
  ↓
RAGConnect (Python + FastAPI)
  ↓
RAGFlow (Local Docker)
  ↓
Local LLM
```

## Project Goal

Build and validate RAGConnect independently before integrating it with SkillFlow.

RAGConnect will provide an application-facing API and abstract the RAGFlow integration from SkillFlow.

## Development Strategy

1. Build RAGConnect independently.
2. Run RAGFlow locally using Docker.
3. Connect RAGConnect to RAGFlow.
4. Validate retrieval and generated responses using a local LLM.
5. Test and evaluate the RAG workflow.
6. Integrate RAGConnect with SkillFlow.
7. Deploy RAGConnect and RAGFlow on Render after the local POC is stable.

## Technology Stack

- Python
- FastAPI
- Uvicorn
- HTTPX
- Pydantic
- Pytest
- Docker
- RAGFlow
- Local LLM

## Integration Principle

SkillFlow will remain unchanged during the initial RAGConnect POC. Once RAGConnect and RAGFlow are validated independently, SkillFlow will integrate with RAGConnect through its Node.js backend.

## Status

Initial project setup.
