from typing import Annotated
from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def list_items():
    return [
        "Item1", "Item2"
    ]

@router.get("/latest/")
def get_last_item():
    return {
        "item": {
            "id": 12332
        }
    }

@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "name": "Some name",
        "id": item_id + 123
    }
