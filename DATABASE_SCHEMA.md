# SahaYatra — Database Schema

## 1. Database

Database name:

sahayatra

Database type:

MongoDB

The backend is responsible for all database operations.

The frontend must never directly access MongoDB.

---

## 2. Collections

The SahaYatra database contains these collections:

1. users
2. trips
3. itineraries
4. bookings
5. disruptions
6. notifications

---

## 3. Users Collection

Collection:

users

Purpose:

Stores user information and travel preferences.

Fields:

userId
- Type: String
- Unique identifier for the user

name
- Type: String
- User's name

email
- Type: String
- User's email address
- Should be unique

preferences
- Type: Object

preferences.budget
- Type: Number

preferences.interests
- Type: Array of Strings

preferences.travelStyle
- Type: String

preferences.preferredTransport
- Type: String

createdAt
- Type: Date

updatedAt
- Type: Date

Example:

{
  "userId": "USER001",
  "name": "Mownica",
  "email": "mownica@example.com",
  "preferences": {
    "budget": 25000,
    "interests": [
      "history",
      "food"
    ],
    "travelStyle": "balanced",
    "preferredTransport": "flight"
  },
  "createdAt": "2026-10-06T10:00:00Z",
  "updatedAt": "2026-10-06T10:00:00Z"
}

---

## 4. Trips Collection

Collection:

trips

Purpose:

Stores the user's travel plans and AeroSync monitoring status.

Fields:

tripId
- Type: String
- Unique identifier

userId
- Type: String
- References users.userId

destination
- Type: String

startDate
- Type: Date

endDate
- Type: Date

budget
- Type: Number

companions
- Type: Number

interests
- Type: Array of Strings

travelStyle
- Type: String

preferredTransport
- Type: String

status
- Type: String

Allowed trip statuses:

PLANNING
GENERATING
READY
MONITORING
DISRUPTED
COMPLETED
CANCELLED

aeroSync
- Type: Object

aeroSync.enabled
- Type: Boolean

aeroSync.status
- Type: String

Possible AeroSync statuses:

INACTIVE
STARTING
ACTIVE
PAUSED
DISRUPTED
ERROR

aeroSync.lastChecked
- Type: Date

createdAt
- Type: Date

updatedAt
- Type: Date

Example:

{
  "tripId": "TRIP001",
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
  "preferredTransport": "flight",
  "status": "READY",
  "aeroSync": {
    "enabled": true,
    "status": "ACTIVE",
    "lastChecked": "2026-10-06T10:00:00Z"
  },
  "createdAt": "2026-10-06T10:00:00Z",
  "updatedAt": "2026-10-06T10:00:00Z"
}

---

## 5. Itineraries Collection

Collection:

itineraries

Purpose:

Stores AI-generated and recovery-generated itinerary versions.

Important rule:

Existing itineraries must never be overwritten after a disruption.

Each new recovery creates a new version.

Fields:

itineraryId
- Type: String
- Unique identifier

tripId
- Type: String
- References trips.tripId

version
- Type: Number

status
- Type: String

Possible statuses:

ACTIVE
SUPERSEDED
DRAFT

generatedBy
- Type: String

Possible values:

PLANNER_AGENT
RECOVERY_AGENT
USER

days
- Type: Array

Each day contains:

date
- Type: Date

activities
- Type: Array

Each activity contains:

activityId
- Type: String

title
- Type: String

type
- Type: String

location
- Type: String

startTime
- Type: Date

endTime
- Type: Date

durationMinutes
- Type: Number

priority
- Type: String

Possible priorities:

LOW
MEDIUM
HIGH

status
- Type: String

Possible activity statuses:

PLANNED
MOVED
CANCELLED
COMPLETED

modifiable
- Type: Boolean

createdAt
- Type: Date

updatedAt
- Type: Date

Example:

{
  "itineraryId": "ITIN001",
  "tripId": "TRIP001",
  "version": 1,
  "status": "ACTIVE",
  "generatedBy": "PLANNER_AGENT",
  "days": [
    {
      "date": "2026-10-18",
      "activities": [
        {
          "activityId": "ACT001",
          "title": "Museum Visit",
          "type": "SIGHTSEEING",
          "location": "National Museum",
          "startTime": "2026-10-18T15:00:00Z",
          "endTime": "2026-10-18T17:00:00Z",
          "durationMinutes": 120,
          "priority": "HIGH",
          "status": "PLANNED",
          "modifiable": true
        }
      ]
    }
  ],
  "createdAt": "2026-10-06T10:00:00Z",
  "updatedAt": "2026-10-06T10:00:00Z"
}

---

## 6. Bookings Collection

Collection:

bookings

Purpose:

Stores travel bookings that AeroSync monitors.

Fields:

bookingId
- Type: String
- Unique identifier

tripId
- Type: String
- References trips.tripId

type
- Type: String

Possible booking types:

FLIGHT
TRAIN
BUS
HOTEL
ACTIVITY
TRANSPORT

provider
- Type: String

flightNumber
- Type: String
- Required for flight bookings

departure
- Type: Date

arrival
- Type: Date

status
- Type: String

Possible flight statuses:

ON_TIME
DELAYED
CANCELLED
BOARDING
COMPLETED
UNKNOWN

delayMinutes
- Type: Number

lastUpdated
- Type: Date

createdAt
- Type: Date

updatedAt
- Type: Date

Example:

{
  "bookingId": "BOOKING001",
  "tripId": "TRIP001",
  "type": "FLIGHT",
  "provider": "Demo Airlines",
  "flightNumber": "AI542",
  "departure": "2026-10-18T09:00:00Z",
  "arrival": "2026-10-18T11:30:00Z",
  "status": "ON_TIME",
  "delayMinutes": 0,
  "lastUpdated": "2026-10-06T10:00:00Z",
  "createdAt": "2026-10-06T10:00:00Z",
  "updatedAt": "2026-10-06T10:00:00Z"
}

---

## 7. Disruptions Collection

Collection:

disruptions

Purpose:

Stores detected travel disruptions and their recovery information.

Fields:

disruptionId
- Type: String
- Unique identifier

tripId
- Type: String
- References trips.tripId

bookingId
- Type: String
- References bookings.bookingId

eventType
- Type: String

Possible event types:

FLIGHT_DELAY
FLIGHT_CANCELLED
TRANSPORT_DELAY
ACTIVITY_CANCELLED
WEATHER_ALERT
BOOKING_CHANGE

severity
- Type: String

Possible severity levels:

LOW
MEDIUM
HIGH
CRITICAL

previousStatus
- Type: String

newStatus
- Type: String

delayMinutes
- Type: Number

oldArrivalTime
- Type: Date

newArrivalTime
- Type: Date

affectedActivities
- Type: Array

Each affected activity contains:

activityId
- Type: String

reason
- Type: String

impact
- Type: String

recovery
- Type: Object

recovery.status
- Type: String

Possible recovery statuses:

PENDING
ANALYZING
GENERATING
COMPLETED
FAILED

recovery.recoveryId
- Type: String

recovery.newItineraryVersion
- Type: Number

detectedAt
- Type: Date

resolvedAt
- Type: Date

Example:

{
  "disruptionId": "DISRUPTION001",
  "tripId": "TRIP001",
  "bookingId": "BOOKING001",
  "eventType": "FLIGHT_DELAY",
  "severity": "HIGH",
  "previousStatus": "ON_TIME",
  "newStatus": "DELAYED",
  "delayMinutes": 90,
  "oldArrivalTime": "2026-10-18T11:30:00Z",
  "newArrivalTime": "2026-10-18T13:00:00Z",
  "affectedActivities": [
    {
      "activityId": "ACT001",
      "reason": "Flight delay reduces available travel time",
      "impact": "MOVE_ACTIVITY"
    }
  ],
  "recovery": {
    "status": "COMPLETED",
    "recoveryId": "RECOVERY001",
    "newItineraryVersion": 2
  },
  "detectedAt": "2026-10-18T08:00:00Z",
  "resolvedAt": "2026-10-18T08:05:00Z"
}

---

## 8. Notifications Collection

Collection:

notifications

Purpose:

Stores in-app and email notifications.

Fields:

notificationId
- Type: String
- Unique identifier

userId
- Type: String
- References users.userId

tripId
- Type: String
- References trips.tripId

disruptionId
- Type: String
- References disruptions.disruptionId

type
- Type: String

Possible notification types:

TRIP_UPDATE
DISRUPTION
ITINERARY_CHANGE
SYSTEM

title
- Type: String

message
- Type: String

read
- Type: Boolean

email
- Type: Object

email.sent
- Type: Boolean

email.sentAt
- Type: Date

createdAt
- Type: Date

Example:

{
  "notificationId": "NOTIFICATION001",
  "userId": "USER001",
  "tripId": "TRIP001",
  "disruptionId": "DISRUPTION001",
  "type": "DISRUPTION",
  "title": "Flight Delay Detected",
  "message": "Your flight AI542 has been delayed by 90 minutes. AeroSync is updating your itinerary.",
  "read": false,
  "email": {
    "sent": true,
    "sentAt": "2026-10-18T08:06:00Z"
  },
  "createdAt": "2026-10-18T08:05:00Z"
}

---

## 9. Database Relationships

Users → Trips

One user can have multiple trips.

users.userId → trips.userId

Trips → Itineraries

One trip can have multiple itinerary versions.

trips.tripId → itineraries.tripId

Trips → Bookings

One trip can have multiple bookings.

trips.tripId → bookings.tripId

Trips → Disruptions

One trip can have multiple disruptions.

trips.tripId → disruptions.tripId

Bookings → Disruptions

A booking can generate multiple disruption records over time.

bookings.bookingId → disruptions.bookingId

Users → Notifications

One user can have multiple notifications.

users.userId → notifications.userId

---

## 10. Recommended MongoDB Indexes

Create these indexes for better query performance:

users.email

trips.userId

bookings.tripId

disruptions.tripId

notifications.userId

notifications.read

itineraries.tripId

itineraries.tripId + version

---

## 11. Data Rules

1. Use UTC timestamps in the backend and database.
2. Every major resource must have a unique ID.
3. Required fields must be validated before database insertion.
4. Email addresses should be unique for users.
5. Itinerary versions must never be overwritten.
6. Old itinerary versions should remain available for comparison.
7. Database operations must happen through the FastAPI backend.
8. Frontend must never directly connect to MongoDB.
9. Sensitive information must not be stored unnecessarily.
10. API keys and secrets must never be stored in MongoDB documents.
11. Database connection strings must be stored in environment variables.

---

## 12. Environment Configuration

MongoDB connection information must be stored in environment variables.

Example:

MONGODB_URI=

DATABASE_NAME=sahayatra

Never commit actual credentials, passwords, or connection strings to GitHub.

---

## 13. Source of Truth

MongoDB is the source of truth for persistent application data.

The following data must be persisted:

- Users
- Trips
- Itineraries
- Bookings
- Disruptions
- Notifications

The frontend should receive persistent data through FastAPI APIs.

---

## 14. AeroSync Data Flow

Booking status changes:

Booking
↓
AeroSync Monitor
↓
Disruption Event
↓
Disruption Collection
↓
Conflict Engine
↓
Recovery Agent
↓
New Itinerary Version
↓
Notification
↓
Database

---

## 15. Main Demo Data Flow

Initial flight:

AI542
Status: ON_TIME
Arrival: 11:30

User itinerary:

15:00 — Museum
18:00 — India Gate
20:00 — Dinner

Simulation:

90-minute flight delay

Updated flight:

AI542
Status: DELAYED
Arrival: 13:00

AeroSync creates a disruption record.

Conflict Engine identifies affected activities.

Recovery Agent creates itinerary Version 2.

Version 1 remains stored.

Version 2 becomes ACTIVE.

A notification is created.

Email status is stored in the notification document.

This allows the complete AeroSync recovery process to be demonstrated and audited.
