from typing import Any, Dict
import requests

class ADKClient:
    def __init__(self, api_key: str, base_url: str = "https://api.google.com/adk"):
        self.api_key = api_key
        self.base_url = base_url

    def send_request(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_data(self, query: str) -> Dict[str, Any]:
        data = {"query": query}
        return self.send_request("data", data)

    def process_response(self, response: Dict[str, Any]) -> Any:
        # Process the response from the ADK service as needed
        return response.get("result")