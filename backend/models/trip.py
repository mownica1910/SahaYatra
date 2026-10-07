from pydantic import BaseModel
from typing import Optional
from datetime import date


class TripCreate(BaseModel):
    userId: str
    destination: str
    startDate: date
    endDate: date
    budget: Optional[float] = None
    companions: int = 1
    interests: list[str] = []
    travelStyle: Optional[str] = None
    preferredTransport: Optional[str] = None