from fastapi import APIRouter, Depends
from app.security import verify_token

router = APIRouter(tags=["Productivity"])

@router.get("/daily-plan", summary="Get Daily Plan")
def daily_plan(auth=Depends(verify_token)):
    return {
        "message": "Fokus hari ini: kerja, olahraga, belajar"
    }