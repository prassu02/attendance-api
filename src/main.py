from fastapi import FastAPI
from src.database import Base, engine

from src.routers import auth, sessions, attendance, monitoring

# Create tables safely
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(sessions.router)
app.include_router(attendance.router)
app.include_router(monitoring.router)


@app.get("/")
def home():
    return {"msg": "API running"}
