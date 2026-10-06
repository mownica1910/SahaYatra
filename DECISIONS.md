# SahaYatra — Architecture Decisions

## 1. Purpose

This document records the important technical and product decisions made for the SahaYatra project.

The purpose is to ensure that all team members follow the same architecture and implementation direction.

Major changes should be discussed with the team and documented here before implementation.

---

## 2. Frontend Technology

Decision:

React + Vite + Tailwind CSS + shadcn/ui

Reason:

React provides a component-based frontend architecture.

Vite provides a fast development environment.

Tailwind CSS allows rapid and consistent styling.

shadcn/ui provides reusable UI components.

Lucide provides consistent icons.

---

## 3. Backend Technology

Decision:

Python + FastAPI + Pydantic

Reason:

FastAPI provides a lightweight and high-performance API framework.

Python integrates well with AI and machine-learning libraries.

Pydantic provides request and response validation.

FastAPI also provides automatic API documentation through Swagger.

---

## 4. Database Technology

Decision:

MongoDB

Reason:

The application contains flexible and nested data such as:

- User preferences
- Trips
- Itineraries
- Activities
- Bookings
- Disruptions
- Notifications

MongoDB is suitable for this flexible document structure.

---

## 5. AI Architecture

Decision:

LangGraph + LangChain + LLM

Reason:

LangGraph allows us to represent agent workflows and state transitions.

LangChain provides integrations and utilities for working with LLMs.

The LLM will handle reasoning and natural-language tasks.

Deterministic application logic will remain in normal backend code.

---

## 6. Primary AI Agents

Decision:

The MVP will use two primary agents.

### Planner Agent

Responsible for:

- Understanding user preferences
- Generating personalized itineraries
- Considering budget
- Considering interests
- Considering travel style
- Considering travel constraints

### Recovery Agent

Responsible for:

- Understanding disruptions
- Analyzing affected activities
- Generating alternative arrangements
- Preserving unaffected activities
- Creating revised itineraries
- Explaining recovery decisions

Additional agents may be added later if they provide clear value.

---

## 7. AeroSync Architecture

Decision:

AeroSync will be implemented as the adaptive trip monitoring and recovery layer.

AeroSync responsibilities:

1. Monitor bookings and trip events
2. Detect disruptions
3. Create disruption records
4. Analyze itinerary impact
5. Trigger recovery
6. Update the itinerary
7. Notify the user

AeroSync is a core differentiating feature of SahaYatra.

---

## 8. Mock Disruption Provider

Decision:

The MVP will use a mock disruption provider for the primary hackathon demonstration.

Reason:

Depending entirely on real airline APIs may introduce:

- API availability issues
- Authentication problems
- Rate limits
- Unpredictable responses
- Internet dependency
- Difficulty reproducing the demo

The mock provider allows the team to reliably demonstrate the complete AeroSync flow.

---

## 9. Main AeroSync Demonstration

Decision:

The primary demonstration will simulate a 90-minute flight delay.

Flow:

Flight ON_TIME
↓
User clicks SIMULATE 90 MIN DELAY
↓
Mock provider changes flight status
↓
AeroSync detects disruption
↓
Conflict Engine analyzes itinerary
↓
Affected activities are identified
↓
Recovery Agent generates recovery plan
↓
New itinerary version is created
↓
Frontend updates
↓
Notification is generated
↓
Email is sent

This is the primary hackathon demonstration scenario.

---

## 10. Itinerary Versioning

Decision:

Itineraries will be versioned.

Example:

Version 1

Original AI-generated itinerary.

Version 2

Itinerary after a flight delay.

Version 3

Itinerary after another disruption.

Reason:

The system should preserve the original plan and provide a clear before-and-after comparison.

Existing itinerary versions must never be silently overwritten.

---

## 11. LLM and Deterministic Logic

Decision:

The LLM will not be responsible for critical deterministic calculations.

### LLM Responsibilities

- Preference interpretation
- Activity reasoning
- Itinerary planning
- Recovery reasoning
- Natural-language explanations

### Code Responsibilities

- Date calculations
- Time calculations
- Conflict detection
- Validation
- Database operations
- API calls
- State management
- Notifications
- Business rules

Reason:

Deterministic operations should remain predictable and testable.

---

## 12. Structured AI Outputs

Decision:

AI outputs used by backend logic must be structured.

The system should use JSON-compatible or Pydantic-validated outputs.

Reason:

Free-form AI text is unreliable for critical application logic.

Structured outputs make the system easier to validate, debug, and integrate with APIs and databases.

---

## 13. Frontend and Backend Communication

Decision:

The frontend communicates with the backend only through REST APIs.

Flow:

React
↓
FastAPI
↓
Services
↓
MongoDB / AI / AeroSync
↓
FastAPI
↓
React

The frontend must never directly connect to MongoDB.

---

## 14. API Contract

Decision:

The API contract is maintained in:

API_CONTRACT.md

Frontend and backend developers must follow the defined API structures.

If an API request or response changes, the API contract must also be updated.

Breaking changes must be discussed before implementation.

---

## 15. Database Source of Truth

Decision:

MongoDB is the source of truth for persistent application data.

Persistent data includes:

- Users
- Trips
- Itineraries
- Bookings
- Disruptions
- Notifications

The frontend may maintain temporary UI state but must not become the source of truth for persistent data.

---

## 16. Notification Strategy

Decision:

The MVP will support:

- In-app notifications
- Email notifications

When a disruption is successfully processed:

1. Disruption is stored.
2. Recovery result is stored.
3. New itinerary version is stored.
4. In-app notification is created.
5. Email notification is attempted.
6. Email delivery status is stored.

---

## 17. Email Reliability

Decision:

Email delivery failure should not prevent itinerary recovery.

If the email service fails:

- The recovery should still be saved.
- The updated itinerary should still be shown in the application.
- The notification should still exist in the database.
- Email failure should be logged.

Reason:

Email is a notification channel and should not become a single point of failure for the core trip recovery system.

---

## 18. MVP Scope

The MVP will prioritize:

- Trip creation
- AI itinerary generation
- Booking creation
- AeroSync monitoring
- Mock disruption
- Conflict detection
- Recovery Agent
- Itinerary versioning
- In-app notifications
- Email notification
- Clean frontend
- End-to-end demonstration

Optional features will only be added after the core flow is stable.

---

## 19. Features Deferred Until Core MVP Works

The following features are optional and should not delay the core implementation:

- Real airline API integration
- Advanced maps
- Live weather integration
- Voice assistant
- Multiple advanced AI agents
- Advanced analytics
- Complex recommendation systems

The team should first make the primary AeroSync flow reliable.

---

## 20. Development Strategy

Decision:

The project will be developed incrementally.

Development flow:

Architecture
↓
API Contract
↓
Database Schema
↓
Backend Module
↓
AI Module
↓
Frontend Module
↓
Integration
↓
Testing
↓
End-to-End Demo

Large untested implementations should be avoided.

---

## 21. AI Coding Tools

Decision:

AI coding tools such as Cursor may be used by all team members.

However:

AI-generated code must be reviewed and tested before being committed.

Rules:

1. Understand the generated code.
2. Run the application.
3. Test the feature.
4. Check API behavior.
5. Check database behavior.
6. Fix errors.
7. Commit only after validation.

AI tools assist development but do not replace engineering decisions.

---

## 22. Git Strategy

Decision:

The project will use GitHub as the source of truth for code and technical documentation.

Main branch:

main

Team members should preferably work on feature branches.

Suggested branches:

backend-mownica
backend-minni
frontend-snehanjali

Feature branches should be tested before merging.

---

## 23. Documentation Strategy

The following files define the core project architecture:

PROJECT_RULES.md
API_CONTRACT.md
DATABASE_SCHEMA.md
DECISIONS.md

These documents should be updated whenever an important architecture or API decision changes.

---

## 24. Security Decisions

The following rules apply:

1. API keys must never be committed to GitHub.
2. Database credentials must never be committed.
3. Secrets must be stored in environment variables.
4. .env files must be ignored by Git.
5. Sensitive information must not be exposed through API responses.
6. Backend validation is required for incoming requests.

---

## 25. Final Product Decision

SahaYatra should not be presented as only an AI itinerary generator.

The core product story is:

AI creates the travel plan.

AeroSync watches the journey.

A disruption occurs.

AeroSync understands the impact.

The Recovery Agent creates a new plan.

The system updates the itinerary.

The user is notified.

Therefore:

SahaYatra = AI Travel Planning + AeroSync Adaptive Recovery

The project's strongest demonstration should show the complete journey from planning to disruption detection to autonomous recovery.
