from typing import Generator
from app.db.base import SessionLocal

# Context manager to get a database session
from contextlib import contextmanager


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
