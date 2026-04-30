from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

# SAFE IMPORTS (to detect error)
try:
    from src.routes.auth import router as auth_router
    app.include_router(auth_router, prefix="/auth")
except Exception as e:
    print("AUTH ROUTE ERROR:", e)

try:
    from src.routes.sessions import router as session_router
    app.include_router(session_router, prefix="/sessions")
except Exception as e:
    print("SESSIONS ROUTE ERROR:", e)

try:
    from src.routes.attendance import router as attendance_router
    app.include_router(attendance_router, prefix="/attendance")
except Exception as e:
    print("ATTENDANCE ROUTE ERROR:", e)

try:
    from src.routes.monitoring import router as monitoring_router
    app.include_router(monitoring_router, prefix="/monitoring")
except Exception as e:
    print("MONITORING ROUTE ERROR:", e)
