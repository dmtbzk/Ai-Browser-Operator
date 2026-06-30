from app.tools.browser_tools import (
    open_browser_page,
    search_browser_web,
    open_search_result,
    extract_page_links,
    get_current_browser_state,
    close_browser_session,
)


TOOL_REGISTRY = {
    "open_browser_page": {
        "description": "Open a web page and return its title, URL and page text.",
        "function": open_browser_page,
        "arguments": {
            "url": "The full URL to open, including https://"
        }
    },
    "search_browser_web": {
        "description": "Search the web and return search result titles and URLs.",
        "function": search_browser_web,
        "arguments": {
            "query": "The search query"
        }
    },
    "open_search_result": {
        "description": "Open a result from the latest search results by index.",
        "function": open_search_result,
        "arguments": {
            "index": "The 1-based search result index"
        }
    },
    "extract_page_links": {
        "description": "Extract links from the currently open page.",
        "function": extract_page_links,
        "arguments": {}
    },
    "get_current_browser_state": {
        "description": "Return the current browser state.",
        "function": get_current_browser_state,
        "arguments": {}
    },
    "close_browser_session": {
        "description": "Close the current browser session.",
        "function": close_browser_session,
        "arguments": {}
    },
}


def get_allowed_tool_names():
    return set(TOOL_REGISTRY.keys())


def get_tool_function(tool_name: str):
    tool = TOOL_REGISTRY.get(tool_name)

    if not tool:
        return None

    return tool["function"]


def get_tools_for_prompt():
    lines = []

    for name, config in TOOL_REGISTRY.items():
        args = config["arguments"]

        if args:
            arg_text = ", ".join(args.keys())
            lines.append(f"- {name}({arg_text}): {config['description']}")
        else:
            lines.append(f"- {name}(): {config['description']}")

    return "\n".join(lines)