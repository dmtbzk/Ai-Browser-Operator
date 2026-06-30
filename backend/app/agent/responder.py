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

    Write a helpful final answer for the user. Follow these rules:
    - If the observations contain URLs or links, always list them clearly with their titles and full URLs.
    - If page content was extracted, summarize the key information.
    - Be concise and structured. Use bullet points or numbered lists where appropriate.
    - Never hide or omit URLs found during browsing.
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )

    return response.output_text