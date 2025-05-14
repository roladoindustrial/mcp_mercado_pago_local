from fastapi.routing import APIRouter
from fastapi import FastAPI
import inspect

def serve_mcp(app: FastAPI, tools: list):
    router = APIRouter()

    @router.get("/schema")
    def get_schema():
        return {
            "tools": [{
                "name": f.__name__,
                "description": f.__doc__,
                "parameters": list(inspect.signature(f).parameters.keys())
            } for f in tools]
        }

    @router.post("/invoke")
    async def invoke(data: dict):
        for f in tools:
            if f.__name__ == data["tool"]:
                return f(**data["parameters"])
        return {"error": "Tool not found"}

    app.include_router(router)
