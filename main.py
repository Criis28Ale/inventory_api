from fastapi import FastAPI, HTTPException
from models import Item
from crud import inventory_crud
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/items", response_model=List[Item])
def list_items():
    return inventory_crud["list"]()

@app.post("/items", response_model=Item)
def create_item(item: Item):
    return inventory_crud["create"](item)

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = inventory_crud["get"](item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    updated = inventory_crud["update"](item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if not inventory_crud["delete"](item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}
