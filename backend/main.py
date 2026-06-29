from fastapi import FastAPI
from app.api.schemas import ChatResponse, ChatRequest
from app.agent.orchestrator import run_agent
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = run_agent(request.message)
    return ChatResponse(answer=answer)