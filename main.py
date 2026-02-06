from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import verify_and_format

app = FastAPI(title="AI Ops Assistant")

class TaskRequest(BaseModel):
    task: str

@app.post("/run-task")
def run_task(req: TaskRequest):
    try:
        plan = create_plan(req.task)

        if "error" in plan:
            return {"status": "failed", "planner_error": plan}

        execution_results = execute_plan(plan)
        final_output = verify_and_format(req.task, plan, execution_results)

        return {
            "plan": plan,
            "execution_results": execution_results,
            "final_output": final_output
        }

    except Exception as e:
        return {"status": "failed", "error": str(e)}

@app.get("/")
def home():
    return {"message": "AI Ops Assistant running. Go to /docs"}
