import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_create_and_get_item():
    # Create item
    item_data = {"name": "Kitty", "description": "Cute cat"}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    items = response.json()
    assert any(i["name"] == "Kitty" for i in items.values())

    # Get all items
    response = client.get("/items/")
    assert response.status_code == 200
    items = response.json()
    assert any(i["name"] == "Kitty" for i in items.values())

    # Get one item
    item_id = list(items.keys())[0]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Kitty"

def test_update_and_delete_item():
    # Create item
    item_data = {"name": "Kitty2", "description": "Another cat"}
    response = client.post("/items/", json=item_data)
    items = response.json()
    item_id = list(items.keys())[-1]

    # Update item
    updated_data = {"name": "KittyUpdated", "description": "Updated cat"}
    response = client.put(f"/items/{item_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "KittyUpdated"

    # Delete item
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    items = response.json()
    assert all(i["name"] != "KittyUpdated" for i in items.values())