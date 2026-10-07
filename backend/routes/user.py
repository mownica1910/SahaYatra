from fastapi import APIRouter, HTTPException
from backend.database.connection import db
from backend.models.user import UserCreate
from datetime import datetime, timezone
import uuid

router = APIRouter(prefix="/api/users", tags=["Users"])

users_collection = db["users"]


@router.post("")
def create_user(user: UserCreate):
    existing_user = users_collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=409, detail="User already exists")

    user_id = "USER" + uuid.uuid4().hex[:8].upper()
    now = datetime.now(timezone.utc)

    user_data = {
        "userId": user_id,
        "name": user.name,
        "email": user.email,
        "preferences": user.preferences.model_dump() if user.preferences else {},
        "createdAt": now,
        "updatedAt": now
    }

    users_collection.insert_one(user_data)
    user_data.pop("_id", None)

    return {
        "success": True,
        "message": "User created successfully",
        "data": user_data
    }

@router.get("/{user_id}")
def get_user(user_id: str):
    user = users_collection.find_one(
        {"userId": user_id},
        {"_id": 0}
    )

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "success": True,
        "data": user
    }