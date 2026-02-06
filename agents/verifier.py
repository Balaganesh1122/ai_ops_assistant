import json
from llm.gemini_client import call_llm

VERIFIER_SYSTEM_PROMPT = """
You are a Verifier Agent.
You receive the user task, the plan, and execution results.

Your job:
- Check if results are complete.
- If any tool returned an error, mention it clearly.
- Return FINAL output in structured JSON:

{
  "task": "...",
  "summary": "...",
  "results": [...],
  "status": "success | partial | failed"
}

Return ONLY valid JSON.
"""

def verify_and_format(task: str, plan: dict, execution_results: list):
    user_prompt = f"""
Task: {task}

Plan:
{json.dumps(plan, indent=2)}

Execution Results:
{json.dumps(execution_results, indent=2)}
"""

    raw = call_llm(VERIFIER_SYSTEM_PROMPT, user_prompt)

    # Clean up markdown code blocks if present
    cleaned = raw.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except Exception:
        return {
            "task": task,
            "status": "failed",
            "summary": "Verifier output invalid JSON",
            "raw": raw
        }
