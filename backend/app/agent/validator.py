from app.tool_registry.registry import get_allowed_tool_names


def validate_plan(plan: dict) -> dict:
    allowed_tools = get_allowed_tool_names()
    validated_steps = []

    for step in plan.get("steps", []):
        tool_name = step.get("tool")
        arguments = step.get("arguments", {})

        if tool_name not in allowed_tools:
            print("Invalid tool skipped:", tool_name)
            continue

        validated_steps.append({
            "tool": tool_name,
            "arguments": arguments
        })

    plan["steps"] = validated_steps

    return plan