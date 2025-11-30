from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
import os

router = APIRouter()

# Configuration for Google ADK
GOOGLE_ADK_API_URL = os.getenv("GOOGLE_ADK_API_URL", "https://api.google.com/adk")
GOOGLE_ADK_API_KEY = os.getenv("GOOGLE_ADK_API_KEY")

class GoogleADKRequest(BaseModel):
    user_id: str
    query: str

class GoogleADKResponse(BaseModel):
    response: str

@router.post("/google-adk/query", response_model=GoogleADKResponse)
def query_google_adk(req: GoogleADKRequest):
    headers = {
        "Authorization": f"Bearer {GOOGLE_ADK_API_KEY}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(GOOGLE_ADK_API_URL, json=req.dict(), headers=headers)
        response.raise_for_status()
        return GoogleADKResponse(response=response.json().get("response"))
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))