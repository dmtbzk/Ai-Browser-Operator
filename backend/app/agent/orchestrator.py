from app.agent.responder import create_respond, create_final_response
from app.agent.executor import execute_tools

def run_agent(user_message: str) -> str:
    response = create_respond(user_message)
    tool_outputs = execute_tools(response)
    if tool_outputs:
        final_response = create_final_response(
            response.id,
            tool_outputs
        )
        return final_response.output_text

    return response.output_text