from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from adk.adk_client import ADKClient
from tools.rule_agent_client import RuleAgentClient
from tools.memory_client import MemoryClient
import os

app = FastAPI(title="Waste Management ADK Agent")

# Environment variables
ADK_API_KEY = os.getenv("ADK_API_KEY")
LOCAL_RULE_AGENT_URL = os.getenv("LOCAL_RULE_AGENT_URL", "http://localhost:8000")
MEMORY_SERVICE_URL = os.getenv("MEMORY_SERVICE_URL", "http://localhost:8001")

# Initialize clients
adk_client = ADKClient(api_key=ADK_API_KEY)
rule_agent_client = RuleAgentClient(base_url=LOCAL_RULE_AGENT_URL)
memory_client = MemoryClient(base_url=MEMORY_SERVICE_URL)

class ChatMessage(BaseModel):
    user_id: str
    message: str

@app.post("/adk/chat")
def handle_chat_message(req: ChatMessage):
    try:
        response = adk_client.send_message(req.user_id, req.message)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/memory/store")
def store_memory(req: dict):
    try:
        response = memory_client.store_memory(req)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/waste-management/rules")
def get_local_rule(req: dict):
    try:
        response = rule_agent_client.get_rule(req)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)