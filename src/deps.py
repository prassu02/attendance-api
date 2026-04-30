from fastapi import HTTPException, Depends, Request
from jose import jwt

SECRET_KEY = "secret"

def get_current_user(request: Request):
    auth = request.headers.get("Authorization")
    if not auth:
        raise HTTPException(status_code=401)

    token = auth.split(" ")[1]
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

def role_required(roles):
    def wrapper(user=Depends(get_current_user)):
        if user["role"] not in roles:
            raise HTTPException(status_code=403)
        return user
    return wrapper