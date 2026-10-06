# SahaYatra — Project Rules

## 1. Project Vision

SahaYatra is an Agentic AI Travel Concierge that helps users plan personalized trips and automatically adapts the itinerary when unexpected travel disruptions occur.

The system should not only generate an itinerary but also monitor the journey, understand disruptions, reason about their impact, re-plan affected activities, and notify the user.

### Core Principle

> AI creates the plan, watches the journey, understands what changes, and acts when something goes wrong.

---

## 2. AeroSync

AeroSync is the adaptive real-time trip recovery layer of SahaYatra.

It handles:

1. Monitoring travel events
2. Detecting disruptions
3. Identifying affected itinerary activities
4. Analyzing conflicts
5. Generating recovery plans
6. Updating the itinerary
7. Notifying the user

### AeroSync Flow

Monitor
↓
Detect Disruption
↓
Analyze Impact
↓
Generate Recovery Plan
↓
Update Itinerary
↓
Notify User

---

## 3. Technology Stack

The following stack is fixed for the MVP.

### Frontend
- React
- Vite
- Tailwind CSS
- shadcn/ui
- Lucide Icons

### Backend
- Python
- FastAPI
- Pydantic

### Database
- MongoDB

### AI
- LangGraph
- LangChain
- LLM

### Development
- Git
- GitHub
- Cursor

### Notifications
- In-app notifications
- Transactional email

Do not change the technology stack without discussing it with the entire team first.

---

## 4. High-Level Architecture

SahaYatra

React UI → FastAPI → Services → MongoDB / AeroSync / AI → FastAPI → React UI

Important Rule:

The frontend must NEVER directly access MongoDB.

Correct flow:

Frontend
↓
FastAPI
↓
Services
↓
MongoDB / AeroSync / AI
↓
FastAPI
↓
Frontend

---

## 5. Team Responsibilities

### Mownica

- FastAPI backend
- Booking APIs
- AeroSync
- Mock flight provider
- Disruption detection
- Event system
- Conflict engine
- Backend integration

### Minni

- MongoDB
- Database schemas
- Planner Agent
- Recovery Agent
- AI prompts
- Structured AI outputs
- Notifications
- Email

### Snehanjali

- React frontend
- UI/UX
- Pages
- Components
- API integration
- AeroSync interface

### Fourth Team Member

- Testing
- Documentation
- PPT
- Demo preparation
- Bug tracking

Responsibilities can be adjusted only after team discussion.

---

## 6. Core User Flow

Create Trip
↓
AI Generates Itinerary
↓
User Views Itinerary
↓
User Adds Flight / Booking
↓
AeroSync Starts Monitoring
↓
Disruption Occurs
↓
AeroSync Detects It
↓
Conflict Analysis
↓
Recovery Agent
↓
New Itinerary Version
↓
Notification
↓
Email

---

## 7. AI Agent Architecture

The MVP uses two primary agents.

### Planner Agent

Responsible for:

- Understanding user preferences
- Generating personalized itineraries
- Considering budget
- Considering travel style
- Considering interests
- Considering travel time
- Producing structured itinerary data

### Recovery Agent

Responsible for:

- Understanding the disruption
- Considering affected activities
- Generating alternative arrangements
- Preserving unaffected activities
- Producing a revised itinerary
- Explaining why the changes were made

---

## 8. LLM vs Code Responsibilities

The LLM should handle:

- User preference interpretation
- Itinerary reasoning
- Activity selection
- Recovery reasoning
- Natural-language explanations

Normal application code should handle:

- Time calculations
- Date calculations
- Conflict detection
- Validation
- Database operations
- API requests
- State transitions
- Notifications
- Deterministic business rules

Do not ask the LLM to perform calculations that can be handled reliably by normal code.

---

## 9. Structured AI Output

AI responses must use structured JSON/Pydantic-compatible outputs whenever they are used by backend logic.

Do not depend on free-form AI text for critical application logic.

Example:

{
  "affectedActivities": [],
  "changes": [],
  "reason": "",
  "confidence": 0.0
}

---

## 10. MongoDB as Source of Truth

MongoDB is the source of truth for:

- Users
- Trips
- Itineraries
- Bookings
- Disruptions
- Notifications

The frontend must not maintain an independent source of truth for persistent application data.

---

## 11. Itinerary Versioning

Existing itineraries must NEVER simply be overwritten after a disruption.

Example:

Version 1 → Original itinerary
Version 2 → After flight delay
Version 3 → After another disruption

This allows the system to demonstrate how AeroSync adapted the trip.

---

## 12. API Rules

The frontend and backend must communicate only through defined REST APIs.

API structures are documented in:

API_CONTRACT.md

If an API response or request structure changes, the API contract must also be updated.

Do not silently change API structures.

---

## 13. AeroSync MVP

For hackathon reliability, AeroSync will initially use a mock disruption provider.

The main demonstration scenario is:

Flight ON_TIME
↓
Simulate 90-minute delay
↓
AeroSync detects delay
↓
Conflict Engine identifies affected activities
↓
Recovery Agent creates revised itinerary
↓
New itinerary version saved
↓
UI updated
↓
Notification generated
↓
Email sent

This simulation is intentional and is part of the MVP demo.

---

## 14. Main Demo Scenario

Example:

Flight:

AI542
Departure: 09:00
Arrival: 11:30
Status: ON_TIME

Original activities:

15:00 — Museum
18:00 — India Gate
20:00 — Dinner

Then:

SIMULATE 90 MIN DELAY

New arrival:

13:00

AeroSync should:

1. Detect the delay
2. Calculate the impact
3. Identify affected activities
4. Ask the Recovery Agent for alternatives
5. Preserve unaffected activities where possible
6. Create itinerary Version 2
7. Save the disruption
8. Notify the user
9. Send an email

This is the primary "money shot" of the project.

---

## 15. Git Rules

### Main Branch

main

The main branch should contain stable code.

### Feature Branches

Suggested branches:

backend-mownica
backend-minni
frontend-snehanjali

Additional feature branches can be created when needed.

### Commit Rules

Use meaningful commit messages.

Good examples:

initialize SahaYatra project
add trip API
add booking API
add AeroSync monitor
add planner agent
add recovery agent
add itinerary UI

Avoid:

update
changes
final
final2
test
abc

---

## 16. Pull Request Rule

Team members should preferably work on their own branches.

Workflow:

Create branch
↓
Develop feature
↓
Run tests
↓
Commit
↓
Push branch
↓
Create Pull Request
↓
Review
↓
Merge into main

Do not directly push unfinished features to main.

---

## 17. AI Coding Rules

Cursor and other AI coding tools may be used.

However:

AI-generated code is NOT considered complete until it has been run and tested.

Before committing AI-generated code:

1. Understand what the code does
2. Run the application
3. Test the feature
4. Check errors
5. Verify database behavior
6. Commit only after validation

Do not blindly accept large AI-generated codebases.

Build one module at a time.

---

## 18. Testing Philosophy

A feature is complete only after testing at multiple levels.

### Level 1 — Code Test

Does the code run without errors?

### Level 2 — API Test

Test through FastAPI Swagger:

/docs

### Level 3 — Database Test

Verify that the expected data is actually stored in MongoDB.

### Level 4 — Frontend Test

Verify the user can perform the action through the UI.

### Level 5 — End-to-End Test

Verify the complete flow works:

UI
↓
API
↓
Backend
↓
Database / AI
↓
API Response
↓
UI

---

## 19. MVP Priority

The team should prioritize functionality over unnecessary features.

### Must Have

- User/trip creation
- AI itinerary generation
- Trip display
- Booking creation
- AeroSync monitoring
- Mock flight disruption
- Conflict detection
- Recovery Agent
- Itinerary versioning
- Notifications
- Email
- Clean UI
- End-to-end demo

### Nice to Have

- Real external travel APIs
- Advanced maps
- Weather APIs
- More agents
- Voice assistant
- Advanced analytics

Do not sacrifice the core flow for optional features.

---

## 20. Development Philosophy

Old approach:

Idea
↓
Generate entire website
↓
Submit

New approach:

Architecture
↓
API Contract
↓
Database Schema
↓
Small Module
↓
AI-Assisted Coding
↓
Run
↓
Test
↓
Commit
↓
Next Module

Every feature must be validated before moving forward.

---

## 21. Source of Truth

GitHub is the project's technical source of truth.

Important project decisions should be documented.

The following files define the project:

PROJECT_RULES.md
API_CONTRACT.md
DATABASE_SCHEMA.md
DECISIONS.md

If an AI tool suggests a major architecture or technology change, the team must discuss it before implementation.

Do not follow conflicting instructions simply because:

"My ChatGPT/Cursor suggested it."

The project documentation and team decisions take priority.

---

## 22. Final Principle

SahaYatra should demonstrate more than an AI-generated travel itinerary.

The core innovation is:

AI creates the plan, watches the journey, understands what changes, and acts when something goes wrong.

AeroSync is what turns SahaYatra from a normal AI travel planner into an adaptive agentic travel system.
