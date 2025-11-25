from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MetricCreate(BaseModel):
    datetime: datetime
    category: str
    value: float
    note: Optional[str] = None


class MetricUpdate(BaseModel):
    value: Optional[float] = None
    note: Optional[str] = None

    class Config:
        from_attributes = True
