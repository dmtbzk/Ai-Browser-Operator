import json
from app.tools.browser_tools import open_browser_page, search_browser_web, close_browser_session, get_current_browser_state, open_search_result, extract_page_links
from app.tool_registry.registry import get_tool_function




def run_tool(tool_name: str, arguments: dict):
    tool_function = get_tool_function(tool_name)

    if tool_function is None:
        return {"error": f"Tool not found: {tool_name}"}
        
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

def execute_plan(plan: dict):
    observations = []

    for step in plan["steps"]:
        tool_name = step["tool"]
        arguments = step["arguments"]

        tool_result = run_tool(tool_name, arguments)

        observations.append({
            "tool": tool_name,
            "arguments": arguments,
            "result": tool_result
        })

    return observations