from openai import OpenAI
from dotenv import load_dotenv
from app.tool_registry.registry import TOOLS

load_dotenv()

client = OpenAI()

def create_respond(user_message: str):
    response = client.responses.create(
        model="gpt-4o-mini",
        messages=user_message,
        tools=TOOLS
    )

def create_final_response(response_id: str, tool_outputs: list):
    response = client.responses.create(
        model="gpt-4o-mini",
        previous_response_id=response_id,
        input=tool_outputs,
    )
