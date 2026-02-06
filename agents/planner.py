import json
from llm.gemini_client import call_llm


PLANNER_SYSTEM_PROMPT = """
You are a Planner Agent in an AI Operations Assistant.
Your job is to convert a user's natural language task into a structured execution plan.

Return ONLY valid JSON with this schema:

{
  "task": "...",
  "steps": [
    {
      "step_id": 1,
      "action": "description",
      "tool": "github_search | weather_check | none",
      "input": { 
        // For github_search: { "query": "search term" }
        // For weather_check: { "city": "city name" }
      }
    }
  ]
}

Rules:
- Use github_search for repo related tasks.
- Use weather_check for weather related tasks.
- Keep steps minimal but complete.
- Do not return any extra text outside JSON.
"""

def create_plan(user_task: str):
    raw = call_llm(PLANNER_SYSTEM_PROMPT, user_task)

    # Clean up markdown code blocks if present
    cleaned = raw.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except Exception:
        return {"error": "Planner output invalid JSON", "raw": raw}
