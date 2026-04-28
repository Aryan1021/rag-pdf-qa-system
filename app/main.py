from fastapi import FastAPI
from app.routes import health, upload, query

app = FastAPI(title="RAG PDF Q&A System")

app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(query.router, prefix="/query", tags=["Query"])

@app.get("/")
def root():
    return {"message": "Welcome to RAG PDF Q&A System"}