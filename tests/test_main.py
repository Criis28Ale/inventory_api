from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_item():
    item = {"id": 1, "name": "Laptop", "quantity": 10}
    response = client.post("/items", json=item)
    assert response.status_code == 200

    get_response = client.get("/items/1")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Laptop"
