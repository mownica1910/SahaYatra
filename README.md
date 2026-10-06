# SahaYatra ✈️

## Agentic AI Travel Concierge with AeroSync

SahaYatra is an AI-powered travel planning and real-time trip recovery platform that creates personalized travel itineraries and intelligently adapts them when unexpected disruptions occur.

Unlike traditional travel planners that stop after generating an itinerary, SahaYatra continuously monitors the journey and takes action when something goes wrong.

> AI creates the plan, watches the journey, understands what changes, and acts when something goes wrong.

---

## 🌍 Problem

Travel plans depend on multiple factors such as flight schedules, transportation, weather, activity timings, and reservations.

A flight delay, cancellation, transport disruption, weather alert, or activity conflict can affect multiple parts of a travel itinerary.

Most travel applications help users create an itinerary, but when a disruption occurs, travellers often have to manually:

- Identify affected activities
- Find alternative timings
- Reorganize transportation
- Check for conflicts
- Update the itinerary
- Manage multiple changes

This makes travel stressful and time-consuming.

---

## 💡 Solution

SahaYatra combines an Agentic AI Travel Concierge with AeroSync, an adaptive real-time trip recovery layer.

The system:

1. Understands the traveller's preferences
2. Generates a personalized itinerary
3. Monitors important trip events
4. Detects disruptions
5. Analyzes their impact
6. Generates a recovery plan
7. Creates a revised itinerary
8. Updates the application
9. Notifies the traveller through in-app and email notifications

The goal is to build a travel assistant that can plan, monitor, reason, adapt, and act.

---

## ✈️ SahaYatra

SahaYatra is the main travel intelligence layer.

Users provide:

- Destination
- Travel dates
- Budget
- Companions
- Interests
- Travel style
- Preferred transportation

The system uses these preferences to generate a personalized itinerary containing activities, transportation, timings, and travel plans.

---

## ⚡ AeroSync

### Adaptive Real-Time Trip Recovery Engine

AeroSync is the key differentiating feature of SahaYatra.

Instead of stopping after itinerary generation, AeroSync continuously monitors the trip for important changes.

AeroSync works through four major stages:

### 1. Perception

Detect changes such as:

- Flight delays
- Flight cancellations
- Transport delays
- Activity cancellations
- Weather alerts
- Booking changes

### 2. Reasoning

Determine:

- What changed?
- Which itinerary activities are affected?
- How severe is the disruption?
- Which activities can remain unchanged?
- Which activities need to be moved or cancelled?

### 3. Planning

Generate the best possible recovery plan while considering:

- Time constraints
- Travel duration
- Activity priority
- User preferences
- Existing reservations
- Available alternatives

### 4. Action

Automatically:

- Create a revised itinerary
- Save a new itinerary version
- Update the application
- Create an in-app notification
- Send an email notification

---

## 🤖 Agentic AI Architecture

SahaYatra uses specialized AI agents for different responsibilities.

### Planner Agent

Responsible for generating the initial travel itinerary.

Input:

User preferences + trip information

Output:

A structured itinerary containing:

- Days
- Activities
- Locations
- Start and end times
- Duration
- Priority
- Modifiability

### Recovery Agent

Responsible for adapting the itinerary after a disruption.

Input:

- Original itinerary
- Disruption event
- Impact analysis
- User preferences
- Available alternatives

Output:

A revised itinerary that attempts to preserve unaffected plans while resolving conflicts.

---

## 🧠 LLM + Deterministic Logic

SahaYatra does not depend on the LLM for every operation.

Responsibilities are divided between AI reasoning and deterministic application logic.

### LLM handles:

- User preference interpretation
- Itinerary generation
- Recovery reasoning
- Alternative selection
- Natural-language explanations

### Application code handles:

- Time calculations
- Conflict detection
- Duration calculations
- Validation
- Database operations
- API processing
- State changes
- Notifications
- Itinerary version management

This approach improves reliability and predictability.

---

## 🔄 Main User Flow

Create Trip
↓
Collect Preferences
↓
Planner Agent
↓
Generate Itinerary v1
↓
User Reviews Trip
↓
Add / Monitor Bookings
↓
AeroSync Monitoring
↓
Disruption Detected
↓
Impact / Conflict Analysis
↓
Recovery Agent
↓
Generate Itinerary v2
↓
Save New Version
↓
Update Application
↓
Notify User

---

## 🚨 Example: Flight Delay Recovery

Consider a trip with:

Flight AI542
Departure: 09:00
Arrival: 11:30

15:00 → Museum Visit
18:00 → India Gate
20:00 → Dinner

AeroSync detects that the flight has been delayed by 90 minutes.

The new arrival time becomes 13:00.

AeroSync then:

1. Detects the delay
2. Identifies the affected itinerary
3. Calculates possible conflicts
4. Sends the disruption information to the Recovery Agent
5. Generates a revised itinerary
6. Preserves unaffected activities wherever possible
7. Saves the new itinerary as Version 2
8. Updates the user's trip
9. Sends notifications

The user does not have to manually rebuild the entire itinerary.

---

## 🔁 Itinerary Versioning

SahaYatra does not overwrite the original itinerary after a disruption.

Instead, itineraries are versioned.

Example:

Itinerary v1
↓
Original plan
↓
Flight Delay
↓
AeroSync Analysis
↓
Recovery Agent
↓
Itinerary v2
↓
Updated plan

This preserves the history of itinerary changes and makes the recovery process easier to understand.

---

## 🏗️ System Architecture

SahaYatra
│
├── React Frontend
│
├── FastAPI Backend
│
├── MongoDB
│
├── AeroSync
│
├── AI Agents
│   ├── Planner Agent
│   └── Recovery Agent
│
└── Notifications
    ├── In-App
    └── Email

Frontend communicates with the backend through REST APIs.

The backend coordinates:

- MongoDB
- AeroSync
- AI agents
- Conflict detection
- Notifications

---

## 🛠️ Technology Stack

### Frontend

- React
- Vite
- Tailwind CSS
- shadcn/ui
- Lucide Icons
- Framer Motion

### Backend

- Python
- FastAPI
- Pydantic

### Database

- MongoDB

### AI

- LangGraph
- LangChain
- Large Language Model

### Communication

- REST APIs
- In-app notifications
- Email notifications

### Development

- Git
- GitHub
- Cursor
- VS Code

---

## 📁 Project Structure

sahayatra/
│
├── frontend/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── services/
│       ├── hooks/
│       └── App.jsx
│
├── backend/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── database/
│   ├── aerosync/
│   │   ├── monitor.py
│   │   ├── event_detector.py
│   │   ├── conflict_engine.py
│   │   ├── event_models.py
│   │   └── simulator.py
│   └── agents/
│
├── PROJECT_RULES.md
├── API_CONTRACT.md
├── DATABASE_SCHEMA.md
├── DECISIONS.md
├── README.md
└── .gitignore

---

## 🗄️ Database

SahaYatra uses MongoDB as the source of truth.

Main collections:

- users
- trips
- itineraries
- bookings
- disruptions
- notifications

Relationships:

User
↓
Trips
├── Itineraries
├── Bookings
└── Disruptions
    ↓
    Recovery
    ↓
    New Itinerary Version

---

## 🔌 API Architecture

The frontend communicates with the backend only through REST APIs.

React Frontend
↓
FastAPI REST API
↓
Backend Services / Agents / AeroSync
↓
MongoDB

The frontend never directly accesses MongoDB.

API specifications are maintained in API_CONTRACT.md.

---

## 📡 AeroSync Demo Simulation

To make the hackathon demonstration reliable, SahaYatra uses a controlled mock disruption provider.

This avoids depending completely on external airline APIs during the live demonstration.

Demo sequence:

Flight Status: ON_TIME
↓
User clicks "Simulate 90 Minute Delay"
↓
Flight Status: DELAYED
↓
AeroSync detects event
↓
Conflict Engine
↓
Recovery Agent
↓
New Itinerary
↓
In-App Alert
↓
Email Notification

This demonstrates the complete adaptive travel workflow in a controlled environment.

---

## 🔐 Reliability Principles

### 1. Structured AI Outputs

AI responses must follow defined schemas instead of relying on uncontrolled text responses.

### 2. Validation

API requests and important AI outputs are validated before being used.

### 3. Deterministic Conflict Detection

Important scheduling conflicts are calculated using application logic instead of depending entirely on the LLM.

### 4. MongoDB as Source of Truth

MongoDB maintains the persistent state of trips, bookings, disruptions, notifications, and itinerary versions.

### 5. Failure Isolation

Email notification failure should not prevent the core recovery process from completing.

### 6. Versioned Itineraries

Original itineraries are preserved when recovery occurs.

### 7. Testing Before Completion

A feature is considered complete only after it has been:

- Run
- Tested through APIs
- Checked for database persistence
- Tested through the frontend
- Verified through the complete end-to-end flow

---

## 🎯 MVP

The Minimum Viable Product focuses on demonstrating the complete adaptive travel experience.

Core features:

- User creation
- Trip creation
- Personalized itinerary generation
- Trip dashboard
- Booking management
- AeroSync monitoring
- Mock flight disruption
- Delay detection
- Conflict analysis
- AI recovery
- Itinerary versioning
- In-app notifications
- Email notifications

---

## 🚀 Future Enhancements

The architecture can later be extended with:

- Real airline APIs
- Real-time weather APIs
- Hotel availability
- Transport APIs
- Automatic booking changes
- Multi-agent travel coordination
- Advanced risk prediction
- What-if disruption simulation
- Emergency travel recovery
- Voice-based travel assistant
- Multi-city trip optimization
- Real-time location awareness

These features are outside the initial MVP unless required by the hackathon.

---

## 👥 Team

### Mownica

Backend + AeroSync + Integration

Responsibilities:

- FastAPI backend
- Booking APIs
- AeroSync
- Mock flight provider
- Disruption detection
- Conflict engine
- Event handling
- Backend/frontend integration

### Minni

Backend + AI + Database

Responsibilities:

- MongoDB
- Database schemas
- Planner Agent
- Recovery Agent
- AI prompts
- Structured AI outputs
- Notifications
- Email integration

### Snehanjali

Frontend + UI/UX

Responsibilities:

- React application
- UI/UX
- Pages and components
- API integration
- Trip dashboard
- AeroSync interface
- Disruption and recovery screens

### Team Member 4

Testing + Documentation + Presentation

Responsibilities:

- Testing
- Documentation
- Demo preparation
- PPT
- Presentation support
- End-to-end validation

---

## 🌱 Development Philosophy

SahaYatra is developed using an incremental engineering approach.

Instead of:

Idea
↓
Generate Entire Website
↓
Submit

We follow:

Architecture
↓
API Contract
↓
Database Schema
↓
Small Module
↓
AI-Assisted Development
↓
Run
↓
Test
↓
Commit
↓
Integrate
↓
Next Module

AI coding tools such as Cursor may be used to accelerate development, but every generated feature must be reviewed, executed, and tested before being considered complete.

---

## 📚 Project Documentation

### PROJECT_RULES.md

Defines the project vision, architecture, technology stack, team ownership, development rules, and MVP scope.

### API_CONTRACT.md

Defines backend API endpoints, request formats, response formats, and HTTP status conventions.

### DATABASE_SCHEMA.md

Defines MongoDB collections, fields, relationships, statuses, and indexes.

### DECISIONS.md

Records important architectural and technical decisions made by the team.

---

## 🔀 Git Workflow

The project uses feature branches.

main
├── backend-mownica
├── backend-minni
├── frontend-snehanjali
└── feature branches

Development workflow:

Create / switch to feature branch
↓
Implement feature
↓
Run and test
↓
Commit meaningful changes
↓
Push branch
↓
Create Pull Request
↓
Review
↓
Merge into main

Direct development on main should be avoided after the initial setup.

---

## 🧪 End-to-End Demo

The primary hackathon demonstration will showcase the following scenario:

1. User creates a Delhi trip
2. AI generates the itinerary
3. Flight AI542 is added
4. AeroSync starts monitoring
5. Flight is initially ON_TIME
6. User simulates a 90-minute delay
7. AeroSync detects the disruption
8. Conflict Engine identifies affected activities
9. Recovery Agent analyzes the situation
10. New itinerary v2 is generated
11. Application displays the updated plan
12. User receives an in-app notification
13. Email notification is sent

This is the core demonstration of SahaYatra's adaptive travel capability.

---

## 🏆 Why SahaYatra?

Traditional travel applications generally focus on:

PLAN → BOOK → TRAVEL

SahaYatra extends this into:

PLAN → MONITOR → UNDERSTAND → ADAPT → ACT

The key differentiator is AeroSync.

SahaYatra does not simply tell travellers what they should do.

It continuously understands the state of their journey and helps the itinerary adapt when reality changes.

---

## 🔮 Vision

The long-term vision of SahaYatra is to become an intelligent travel companion capable of managing the complexity of real-world travel.

From planning the journey to handling unexpected disruptions, SahaYatra aims to reduce the cognitive load on travellers and make travel more resilient.

> SahaYatra — Plan the journey. Adapt to reality. Keep moving.

---

## 📌 Project Status

🚧 Currently under active development for the hackathon.

The MVP is being developed incrementally with a strong focus on:

- Reliability
- Agentic AI
- Real-time adaptation
- Clean architecture
- End-to-end integration
- Demonstrable functionality

---

## 📄 License

This project is currently developed as a hackathon project.

License and open-source terms may be added later based on the team's decision.
