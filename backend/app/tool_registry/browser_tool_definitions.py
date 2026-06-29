BROWSER_TOOL_DEFINITIONS = [
    {
        "type": "function",
        "name": "open_browser_page",
        "description": "Open a browser page and return the page title and final URL.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The full URL to open, including https://"
                }
            },
            "required": ["url"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "search_browser_web",
        "description": "Search the web for information based on a query.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to perform"
                }
            },
            "required": ["query"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "close_browser_session",
        "description": "Close the browser and return a status message.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "get_current_browser_state",
        "description": "Returns the current browser state including current URL, page title and last search results.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }
    }
]