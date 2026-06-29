import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


AVAILABLE_TOOLS = [
    "open_browser_page",
    "search_browser_web",
    "open_search_result",
    "extract_page_links",
    "get_current_browser_state",
    "close_browser_session",
]


def create_plan(user_message: str):
    prompt = f"""
    You are a browser task planner.

    Your job is to convert the user's request into a JSON plan.

    You do NOT answer the user.
    You do NOT execute tools.
    You ONLY return valid JSON.

    Available tools:
    - open_browser_page(url)
    - search_browser_web(query)
    - open_search_result(index)
    - extract_page_links()
    - get_current_browser_state()
    - close_browser_session()

    Rules:
    - If the user asks to search or find something, use search_browser_web.
    - If the user asks to open the first/second/third result, use open_search_result.
    - If the user asks about the current browser state, use get_current_browser_state.
    - If the user asks to show links on the current page, use extract_page_links.
    - If the user asks to close the browser, use close_browser_session.
    - If the user gives a direct URL, use open_browser_page.
    - Return only JSON. No markdown.

    User request:
    {user_message}

    Expected format:
    {{
    "goal": "user goal",
    "steps": [
        {{
        "tool": "tool_name",
        "arguments": {{}}
        }}
    ]
    }}
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )

    return json.loads(response.output_text)