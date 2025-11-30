from fastapi.testclient import TestClient
from src.main_agent import app

client = TestClient(app)

def test_get_local_rule():
    response = client.post("/waste-management/rules", json={"user_id": "test_user", "query": "What are the waste disposal rules?"})
    assert response.status_code == 200
    assert "rules" in response.json()

def test_store_memory():
    response = client.post("/memory/store", json={"key": "test_key", "value": "test_value"})
    assert response.status_code == 200
    assert response.json() == {"success": True}  # Adjust based on actual response structure

def test_get_local_rule_invalid():
    response = client.post("/waste-management/rules", json={"user_id": "test_user"})
    assert response.status_code == 422  # Unprocessable Entity for missing query

def test_store_memory_invalid():
    response = client.post("/memory/store", json={"key": "test_key"})
    assert response.status_code == 422  # Unprocessable Entity for missing value