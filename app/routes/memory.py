from fastapi import APIRouter
import json
import os

router = APIRouter(tags=["Memory"])

FILE = "memory.json"


def load_memory():
    if not os.path.exists(FILE):
        return {"notes": []}

    with open(FILE, "r") as f:
        return json.load(f)


def save_memory(data):
    with open(FILE, "w") as f:
        json.dump(data, f)


@router.get("/memory")
def get_memory():
    return load_memory()


@router.post("/memory")
def add_memory(note: str):
    data = load_memory()
    data["notes"].append(note)
    save_memory(data)

    return {
        "status": "saved",
        "note": note
    }


@router.get("/memory/latest")
def latest_memory():
    data = load_memory()

    if not data["notes"]:
        return {"note": ""}

    return {
        "note": data["notes"][-1]
    }