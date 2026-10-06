# SahaYatra — API Contract

## 1. Base URL

All backend APIs use:

/api

Example:

/api/trips

---

## 2. Response Format

### Success Response

{
  "success": true,
  "data": {},
  "message": "Success"
}

### Error Response

{
  "success": false,
  "error": {
    "code": "TRIP_NOT_FOUND",
    "message": "Trip not found"
  }
}

---

## 3. Users

### Create User

POST

/api/users

Request:

{
  "name": "Mownica",
  "email": "user@example.com"
}

### Get User

GET

/api/users/{user_id}

---

## 4. Trips

### Create Trip

POST

/api/trips

Request:

{
  "userId": "USER001",
  "destination": "Delhi",
  "startDate": "2026-10-18",
  "endDate": "2026-10-22",
  "budget": 25000,
  "companions": 2,
  "interests": [
    "history",
    "food"
  ],
  "travelStyle": "balanced",
  "preferredTransport": "flight"
}

### Get User Trips

GET

/api/trips?userId=USER001

### Get Trip

GET

/api/trips/{trip_id}

### Delete Trip

DELETE

/api/trips/{trip_id}

### Generate Itinerary

POST

/api/trips/{trip_id}/generate

### Get Itinerary

GET

/api/trips/{trip_id}/itinerary

---

## 5. Bookings

### Create Booking

POST

/api/bookings

Request:

{
  "tripId": "TRIP001",
  "type": "FLIGHT",
  "provider": "Demo Airlines",
  "flightNumber": "AI542",
  "departure": "2026-10-18T09:00:00",
  "arrival": "2026-10-18T11:30:00",
  "status": "ON_TIME"
}

### Get Trip Bookings

GET

/api/trips/{trip_id}/bookings

### Get Booking

GET

/api/bookings/{booking_id}

### Update Booking

PUT

/api/bookings/{booking_id}

---

## 6. AeroSync

### Start AeroSync Monitoring

POST

/api/aerosync/start/{trip_id}

### Get AeroSync Status

GET

/api/aerosync/{trip_id}/status

---

## 7. Demo Disruption APIs

These APIs are used for the hackathon demonstration.

### Simulate Flight Delay

POST

/api/demo/flight-delay

Request:

{
  "bookingId": "BOOKING001",
  "delayMinutes": 90
}

Expected behavior:

1. Flight delay is recorded.
2. AeroSync detects the disruption.
3. Conflict engine analyzes the itinerary.
4. Affected activities are identified.
5. Recovery Agent generates a revised itinerary.
6. A new itinerary version is created.
7. Notification is generated.
8. Email notification is sent.

### Simulate Flight Cancellation

POST

/api/demo/flight-cancel

Request:

{
  "bookingId": "BOOKING001"
}

---

## 8. Disruptions

### Get Trip Disruptions

GET

/api/trips/{trip_id}/disruptions

### Get Disruption

GET

/api/disruptions/{disruption_id}

### Recover From Disruption

POST

/api/disruptions/{disruption_id}/recover

---

## 9. Notifications

### Get User Notifications

GET

/api/users/{user_id}/notifications

### Mark Notification as Read

PUT

/api/notifications/{notification_id}/read

---

## 10. HTTP Status Codes

Use these standard status codes:

200 — Successful request

201 — Resource created

400 — Bad request

404 — Resource not found

409 — Conflict

422 — Validation error

500 — Internal server error

---

## 11. API Rules

1. Frontend communicates with backend only through these APIs.
2. Frontend must never directly access MongoDB.
3. Backend must validate all incoming requests.
4. API responses should follow the standard response format.
5. Breaking API changes must be discussed with the team.
6. If an API changes, this document must also be updated.
7. Never expose API keys or secrets in API responses.
8. Use UTC timestamps in backend/database operations.
