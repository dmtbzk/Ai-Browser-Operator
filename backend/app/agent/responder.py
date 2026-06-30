from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def summarize_observations(user_message: str, plan: dict, observations: list):
    prompt = f"""
    User request:
    {user_message}

    Plan:
    {plan}

    Browser observations:
    {observations}

    Write a helpful final answer for the user.
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )

    return response.output_text