from typing import Any, Dict
import requests
import os

class MemoryClient:
    def __init__(self):
        self.memory_service_url = os.getenv("MEMORY_SERVICE_URL", "http://localhost:8001")

    def store_memory(self, user_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        payload = {
            "user_id": user_id,
            "data": data
        }
        try:
            response = requests.post(f"{self.memory_service_url}/memory/long/set", json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error storing memory: {str(e)}")

    def retrieve_memory(self, user_id: str) -> Dict[str, Any]:
        try:
            response = requests.get(f"{self.memory_service_url}/memory/long/get", params={"user_id": user_id})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error retrieving memory: {str(e)}")