from typing import Dict, Any
import requests
from fastapi import HTTPException

class RuleAgentClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_rule(self, user_id: str, query: str) -> Dict[str, Any]:
        try:
            response = requests.post(f"{self.base_url}/rules", json={"user_id": user_id, "query": query})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=str(e))