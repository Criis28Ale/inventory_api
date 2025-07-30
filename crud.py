from typing import List, Optional
from models import Item

inventory: List[Item] = []

def create(item: Item):
    inventory.append(item)
    return item

def list_items():
    return inventory

def get(item_id: int) -> Optional[Item]:
    for item in inventory:
        if item.id == item_id:
            return item
    return None

def update(item_id: int, item: Item):
    for idx, existing in enumerate(inventory):
        if existing.id == item_id:
            inventory[idx] = item
            return item
    return None

def delete(item_id: int):
    global inventory
    before = len(inventory)
    inventory = [item for item in inventory if item.id != item_id]
    return len(inventory) < before

inventory_crud = {
    "create": create,
    "list": list_items,
    "get": get,
    "update": update,
    "delete": delete,
}
