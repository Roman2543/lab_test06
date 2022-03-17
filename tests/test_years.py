from fastapi.testclient import TestClient
import sys
sys.path.insert(0,'../lab_test06')
from main import app

client = TestClient(app)
def test_year_test_api():
    input = "2540"
    output = 25
    response =client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json()== {"age": output}

def test_input_low():
    input = "-1"
    output ="Your input lower"
    response =client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json()== {"age":output }

def test_input_high():
    input = "2569"
    output ="Your input higher"
    response =client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json()== {"age":output }