from fastapi import APIRouter, Depends
from datetime import datetime

from app.security import verify_token
from app.database.memory_db import memories

router = APIRouter(tags=["Focus"])


@router.get("/focus")
def focus(auth=Depends(verify_token)):
    now = datetime.now().hour

    latest_memory = ""
    if memories:
        latest_memory = memories[-1]["note"]

    if now < 11:
        msg = "Kerjakan tugas paling penting pagi ini."
    elif now < 17:
        msg = "Selesaikan target utama hari ini."
    else:
        msg = "Rapikan hari ini dan siapkan besok."

    if latest_memory:
        msg += f" Fokus utama Anda: {latest_memory}"

    return {"message": msg}