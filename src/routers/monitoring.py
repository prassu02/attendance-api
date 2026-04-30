from fastapi import APIRouter, HTTPException, Request
from src.deps import get_user, require

router = APIRouter()

@router.get("/monitoring/attendance")
def get_monitoring(request: Request):
    require(["monitoring"])(request)
    return {"data": "ok"}

@router.post("/monitoring/attendance")
def block():
    raise HTTPException(status_code=405)
