from fastapi import APIRouter, HTTPException, Request
from jose import jwt

router = APIRouter()

SECRET_KEY = "secret"

def verify(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401)

    token = token.split(" ")[1]
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    if payload.get("role") != "monitoring":
        raise HTTPException(status_code=401)

@router.get("/monitoring/attendance")
def get_data(request: Request):
    verify(request)
    return {"data": "monitoring"}

@router.post("/monitoring/attendance")
def blocked():
    raise HTTPException(status_code=405)