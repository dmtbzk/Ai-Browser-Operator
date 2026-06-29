from fastapi import FastAPI
from app.api.schemas import chatResponse, chatRequest

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: chatRequest):
    return chatResponse(answer=request.message)