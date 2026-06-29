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
    }
]