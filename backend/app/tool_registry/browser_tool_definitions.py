BROWSER_TOOL_DEFINITIONS = [
    {
        "type": "function",
        "name": "open_browser_page",
        "description": "Open a browser page",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string", 
                    "description": "The URL to open"
                    },
            "required": ["url"],
            },
        },
    }
]