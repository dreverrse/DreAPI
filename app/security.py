import os
from dotenv import load_dotenv
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
DEV_MODE = os.getenv("DEV_MODE", "true")

security = HTTPBearer(auto_error=False)


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    if DEV_MODE.lower() == "true":
        return True

    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    if credentials.credentials != API_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    return True