import json
from openai import OpenAI
from dotenv import load_dotenv
from app.prompts.planner_prompt import PLANNER_PROMPT
from app.tool_registry.registry import get_tools_for_prompt

load_dotenv()

client = OpenAI()



def create_plan(user_message: str):
    prompt = PLANNER_PROMPT.format(
        available_tools=get_tools_for_prompt(),
        user_message=user_message
    )

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )

    planner_text = response.output_text

    print("PLANNER RAW OUTPUT:", planner_text)

    try:

        plan = json.loads(planner_text)

    except json.JSONDecodeError:

        print("Planner returned invalid JSON")

        plan = {
            "goal": user_message,
            "steps": []
        }

  

    return plan