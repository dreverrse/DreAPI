from fastapi import APIRouter, Depends
from app.security import verify_token
from datetime import datetime, timedelta

router = APIRouter(tags=["Productivity"])

@router.get("/smart-plan")
def smart_plan(auth=Depends(verify_token)):
    now = datetime.utcnow() + timedelta(hours=7)
    hour = now.hour

    if hour < 12:
        msg = "Pagi ini fokus mulai kerja dan susun target."
    elif hour < 18:
        msg = "Sore ini cek progres dan lanjutkan tugas penting."
    else:
        msg = "Malam ini evaluasi hasil hari ini dan siapkan besok."

    return {"message": msg}