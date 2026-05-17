from fastapi import FastAPI
from pydantic import BaseModel

from backend.graph import build_graph

app = FastAPI()

graph = build_graph()


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():

    return {
        "status": "Backend working"
    }


@app.post("/research")
def run_research(req: QueryRequest):

    try:

        result = graph.invoke({
            "input": req.query
        })

        return {
            "success": True,
            "plan": str(result.get("plan", "")),
            "analysis": str(result.get("analysis", "")),
            "report": str(result.get("report", ""))
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }