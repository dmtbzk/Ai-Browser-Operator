from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.schemas import ChatResponse, ChatRequest
from app.agent.orchestrator import run_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type"],
)

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