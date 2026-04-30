from fastapi import APIRouter, Depends
from src.deps import role_required

router = APIRouter()

@router.post("/attendance/mark")
def mark(user=Depends(role_required(["student"]))):
    return {"message": "Attendance marked"}