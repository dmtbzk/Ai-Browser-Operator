from fastapi import FastAPI
from app.api.schemas import chatResponse, chatRequest
from app.agent.orchestrator import run_agent
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: chatRequest):
    answer = run_agent(request.message)
    return ChatResponse(answer=answer)