from fastapi import APIRouter, HTTPException, Request
from src.deps import get_user, require
from src.auth import create_token

router = APIRouter()

API_KEY = "MY_SECRET_KEY"


@router.post("/auth/monitoring-token")
def monitoring_token(request: Request, key: str):
    user = get_user(request)

    if user["role"] != "monitoring_officer":
        raise HTTPException(status_code=403, detail="Not allowed")

    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return {"token": create_token({"role": "monitoring"}, 1)}


@router.get("/monitoring/attendance")
def get_monitoring(request: Request):
    require(["monitoring"])(request)
    return {"data": "readonly monitoring data"}


@router.post("/monitoring/attendance")
def block_post():
    raise HTTPException(status_code=405, detail="Not allowed")
