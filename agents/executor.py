from tools.github_tool import search_repositories
from tools.weather_tool import get_weather

def execute_plan(plan: dict):
    results = []

    for step in plan.get("steps", []):
        tool = step.get("tool")
        step_input = step.get("input", {})

        if tool == "github_search":
            query = step_input.get("query", "")
            output = search_repositories(query)

        elif tool == "weather_check":
            city = step_input.get("city") or step_input.get("location", "")
            output = get_weather(city)

        else:
            output = {"message": "No tool required"}

        results.append({
            "step_id": step.get("step_id"),
            "action": step.get("action"),
            "tool": tool,
            "input": step_input,
            "output": output
        })

    return results
