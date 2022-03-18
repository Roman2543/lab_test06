from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../lab_test06')        
from main import app

client = TestClient(app)

def test_post_todo_insert(db):
    response = client.post(
        "/",
        json={
            "name": "string2",
            "description": "string",
            "completed": "true",
            "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "string2"
    assert response.json()[0]["description"] == "string"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"

def test_put_todo_update(db):
    response = client.put(
        "/6233fa4fdafac261d4ceacf0",
        json={
            "name": "update",
            "description": "string2",
            "completed": "true",
            "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "update"
    assert response.json()[0]["description"] == "string2"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"

def test_todo_delete(db):
    response = client.delete(
        "/6233fa4fdafac261d4ceacf0"
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
