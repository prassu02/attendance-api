from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

# DEBUG IMPORTS
try:
    from src.routes.auth import router as auth_router
    from src.routes.sessions import router as session_router
    from src.routes.attendance import router as attendance_router
    from src.routes.monitoring import router as monitoring_router

    app.include_router(auth_router, prefix="/auth")
    app.include_router(session_router, prefix="/sessions")
    app.include_router(attendance_router, prefix="/attendance")
    app.include_router(monitoring_router, prefix="/monitoring")

except Exception as e:
    print("🔥 IMPORT ERROR:", e)
