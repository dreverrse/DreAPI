from fastapi import APIRouter, Depends
from datetime import datetime, timedelta
from app.config import USER_NAME, MAIN_GOALS
from app.security import verify_token

router = APIRouter(tags=["Personal"])
    
@router.get("/my-day", summary="Get Personal Daily Briefing")

def my_day(auth=Depends(verify_token)):
    now = datetime.utcnow() + timedelta(hours=7)
    hour = now.hour

    if hour < 12:
        intro = f"Selamat pagi {USER_NAME}. Fokus mulai hari ini."
    elif hour < 18:
        intro = f"Sore {USER_NAME}. Cek progres hari ini."
    else:
        intro = f"Malam {USER_NAME}. Saatnya evaluasi."

    return {
        "message": intro,
        "goals": MAIN_GOALS
    }