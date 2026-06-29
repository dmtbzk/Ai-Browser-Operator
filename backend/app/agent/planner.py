def create_plan(user_message: str):
    message = user_message.lower()

    if "close" in message and "browser" in message:
        return {
            "goal": user_message,
            "steps": [
                {
                    "tool": "close_browser_session",
                    "arguments": {}
                }
            ]
        }

    if "state" in message or "current browser" in message:
        return {
            "goal": user_message,
            "steps": [
                {
                    "tool": "get_current_browser_state",
                    "arguments": {}
                }
            ]
        }

    if "first result" in message:
        return {
            "goal": user_message,
            "steps": [
                {
                    "tool": "open_search_result",
                    "arguments": {
                        "index": 1
                    }
                }
            ]
        }

    if "second result" in message:
        return {
            "goal": user_message,
            "steps": [
                {
                    "tool": "open_search_result",
                    "arguments": {
                        "index": 2
                    }
                }
            ]
        }

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