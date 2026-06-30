from app.agent.planner import create_plan
from app.agent.executor import execute_plan
from app.agent.responder import summarize_observations
from app.agent.validator import validate_plan

def run_agent(user_message: str) -> str:
    plan = create_plan(user_message)
    print("PLAN:", plan)

    validated_plan = validate_plan(plan)
    print("VALIDATED PLAN:", validated_plan)

    observations = execute_plan(validated_plan)
    print("OBSERVATIONS:", observations)

    return summarize_observations(
        user_message,
        validated_plan,
        observations
    )