import json
from app.tools.browser_tools import open_browser_page, search_browser_web, close_browser_session, get_current_browser_state, open_search_result

TOOL_FUNCTIONS = {
    "open_browser_page": open_browser_page,
    "search_browser_web": search_browser_web,
    "close_browser_session": close_browser_session,
    "get_current_browser_state": get_current_browser_state,
    "open_search_result": open_search_result,
}


def run_tool(tool_name: str, arguments: dict):

    if tool_name not in TOOL_FUNCTIONS:
        return {"error": "Tool not found"}

    tool_function = TOOL_FUNCTIONS[tool_name]
    return tool_function(**arguments)

def execute_tools(reponse):
    tool_outputs = []
    for item in reponse.output:
        if item.type == "function_call":
            arguments = json.loads(item.arguments)
            tool_result = run_tool(item.name, arguments)
            tool_outputs.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": str(tool_result)
            })
    return tool_outputs