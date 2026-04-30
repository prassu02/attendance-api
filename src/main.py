from fastapi import FastAPI
from src.routers import auth, sessions, attendance, monitoring

app = FastAPI()

app.include_router(auth.router)
app.include_router(sessions.router)
app.include_router(attendance.router)
app.include_router(monitoring.router)

@app.get("/")
def home():
    return {"msg": "running"}