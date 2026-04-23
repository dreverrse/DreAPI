from fastapi import APIRouter, Depends

router = APIRouter(tags=["System"])

@router.get("/health", summary="Check API Health")
def health_check():
    return {"status": "ok"}