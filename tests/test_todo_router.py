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
