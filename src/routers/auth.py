from fastapi import APIRouter, Depends
from src.auth import create_token

router = APIRouter(prefix="/auth")

@router.post("/signup")
def signup():
    return {"token": create_token({"role": "student"})}

@router.post("/login")
def login():
    return {"token": create_token({"role": "trainer"})}