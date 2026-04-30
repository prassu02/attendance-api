import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")

# fallback (prevents crash)
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./test.db"

# fix postgres:// issue
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

try:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True
    )
except Exception as e:
    print("DB ERROR:", e)
    engine = create_engine("sqlite:///./fallback.db")

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
