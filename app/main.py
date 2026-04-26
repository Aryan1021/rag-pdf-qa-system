from fastapi import FastAPI

app = FastAPI(title="RAG PDF Q&A System")

@app.get("/")
def root():
    return {"message": "RAG API is running"}