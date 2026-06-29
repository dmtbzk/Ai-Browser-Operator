def create_plan(user_message: str):
    message = user_message.lower()

    if "search" in message or "find" in message:
        return {
            "goal": user_message,
            "steps": [
                {
                    "tool": "search_browser_web",
                    "arguments": {
                        "query": user_message
                    }
                }
            ]
        }

    return {
        "goal": user_message,
        "steps": []
    }