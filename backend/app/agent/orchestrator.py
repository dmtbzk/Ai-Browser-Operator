from app.agent.planner import create_plan
from app.agent.executor import execute_plan
from app.agent.responder import summarize_observations


def run_agent(user_message: str) -> str:
    plan = create_plan(user_message)
    print("PLAN:", plan)

    observations = execute_plan(plan)
    print("OBSERVATIONS:", observations)

    return summarize_observations(
        user_message,
        plan,
        observations
    )