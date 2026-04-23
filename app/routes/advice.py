from fastapi import APIRouter, Depends
from datetime import datetime

from app.security import verify_token
from app.database.memory_db import memories

router = APIRouter(tags=["Advice"])


@router.get("/advice")
def advice(auth=Depends(verify_token)):
    now = datetime.now().hour

    latest_memory = ""
    if memories:
        latest_memory = memories[-1]["note"]

    tasks = []

    if now < 11:
        tasks.append("Prioritaskan kerja utama pagi ini")
    elif now < 17:
        tasks.append("Fokus selesaikan tugas penting siang ini")
    else:
        tasks.append("Rapikan hari ini dan tutup tugas malam ini")

    if latest_memory:
        tasks.append(f"Catatan penting: {latest_memory}")

    tasks.append("Latihan tubuh minimal 15 menit")
    tasks.append("Belajar skill 30 menit")

    return {"message": tasks}