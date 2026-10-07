from pydantic import BaseModel, EmailStr
from typing import Optional


class UserPreferences(BaseModel):
    budget: Optional[float] = None
    interests: list[str] = []
    travelStyle: Optional[str] = None
    preferredTransport: Optional[str] = None


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    preferences: Optional[UserPreferences] = None