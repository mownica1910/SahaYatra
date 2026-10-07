from fastapi import APIRouter, HTTPException
from backend.database.connection import db
from backend.models.trip import TripCreate
from datetime import datetime, timezone
import uuid

router = APIRouter(prefix="/api/trips", tags=["Trips"])

trips_collection = db["trips"]
users_collection = db["users"]


@router.post("")
def create_trip(trip: TripCreate):
    user = users_collection.find_one({"userId": trip.userId})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if trip.endDate < trip.startDate:
        raise HTTPException(
            status_code=400,
            detail="End date cannot be before start date"
        )

    trip_id = "TRIP" + uuid.uuid4().hex[:8].upper()
    now = datetime.now(timezone.utc)

    trip_data = {
        "tripId": trip_id,
        "userId": trip.userId,
        "destination": trip.destination,
        "startDate": trip.startDate.isoformat(),
        "endDate": trip.endDate.isoformat(),
        "budget": trip.budget,
        "companions": trip.companions,
        "interests": trip.interests,
        "travelStyle": trip.travelStyle,
        "preferredTransport": trip.preferredTransport,
        "status": "PLANNING",
        "aerosync": {
            "enabled": False,
            "status": "INACTIVE",
            "lastChecked": None
        },
        "createdAt": now,
        "updatedAt": now
    }

    trips_collection.insert_one(trip_data)
    trip_data.pop("_id", None)

    return {
        "success": True,
        "message": "Trip created successfully",
        "data": trip_data
    }


@router.get("/{trip_id}")
def get_trip(trip_id: str):
    trip = trips_collection.find_one(
        {"tripId": trip_id},
        {"_id": 0}
    )

    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    return {
        "success": True,
        "data": trip
    }
@router.get("")
def get_user_trips(userId: str):
    trips = list(
        trips_collection.find(
            {"userId": userId},
            {"_id": 0}
        )
    )

    return {
        "success": True,
        "data": trips
    }