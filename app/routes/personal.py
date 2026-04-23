from fastapi import APIRouter, Depends
from app.security import verify_token
from app.config import USER_NAME, MAIN_GOALS

router = APIRouter()

@router.get("/personal-plan")
def personal_plan(auth=Depends(verify_token)):
    return {
        "user": USER_NAME,
        "message": f"Halo {USER_NAME}, fokus utama hari ini.",
        "goals": MAIN_GOALS
    }