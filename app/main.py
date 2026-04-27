from fastapi import FastAPI
from app.routes import health

app = FastAPI(title="RAG PDF Q&A System")

# Include routers
app.include_router(health.router, prefix="/health", tags=["Health"])

@app.get("/")
def root():
    return {"message": "Welcome to RAG PDF Q&A System"}