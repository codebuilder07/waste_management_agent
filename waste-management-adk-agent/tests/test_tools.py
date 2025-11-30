from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
from tools.rule_agent_client import get_rule
from tools.memory_client import store_memory

app = FastAPI()

@app.post("/test/rule")
def test_get_rule(user_id: str, query: str):
    return get_rule(user_id, query)

@app.post("/test/memory/store")
def test_store_memory(data: dict):
    return store_memory(data)

client = TestClient(app)

def test_get_rule_success():
    response = client.post("/test/rule", json={"user_id": "test_user", "query": "test_query"})
    assert response.status_code == 200
    assert "rule" in response.json()

def test_store_memory_success():
    response = client.post("/test/memory/store", json={"key": "test_key", "value": "test_value"})
    assert response.status_code == 200
    assert response.json() == {"status": "success"}