# 🪐 ASTRA-1 — Mars Mission Control

A centralized emergency operations dashboard designed to help mission operators monitor and respond to a simulated crisis on the Mars colony Astra-1.

## 🚨 Problem Statement

The Astra-1 Mars colony, with a population of 10,000, is experiencing a severe energy storm.

The crisis has caused:

- ⚡ Energy-system instability
- 🫁 Reduced oxygen production
- 📡 Communication disruption
- 🤖 Autonomous-system failures
- 📉 Depletion of essential resources
- 🪐 Loss of reliable contact with ASTRA, the colony's emergency protector

ASTRA must be located within a limited mission window while an unknown underground structure with a similar energy signature creates an additional potential threat.

Mission operators need a centralized system to monitor the crisis, coordinate robots, record emergencies, recover communications, locate ASTRA, and support mission decisions.

## 💡 Proposed Solution

ASTRA-1 Mission Control provides a centralized dashboard that combines mission monitoring, robot coordination, emergency triage, communication recovery, and mission recommendations.

The system follows the workflow:

**SENSE → ANALYZE → PRIORITIZE → ACT → ADAPT**

## ✨ Key Features

### 🚨 Mission Monitoring
- Real-time-style mission status dashboard
- Oxygen and communication status
- ASTRA signal monitoring
- Mission telemetry visualization

### 🤖 Robot Operations
- Select available robots
- Send operational commands
- Store commands in Firestore

### 🏥 Emergency Triage
- Record crew/patient cases
- Assign severity levels
- Store emergency records for mission tracking

### 📡 Communication Recovery
- Select communication channels
- Execute recovery actions
- Store recovery actions in Firestore

### 🧠 Mission Recommendation
- Retrieves current mission conditions
- Analyzes mission status
- Generates a recommended operational response

### 🪐 Mission Visualization
- Mars-themed mission-control interface
- Radar and signal visualization
- Space/Mars animations

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Django + Django REST Framework |
| Database | Firebase Firestore |
| Language | Python |
| API Communication | REST API |
| Development | VS Code |

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │   Streamlit UI      │
                    │  Mission Dashboard  │
                    └──────────┬──────────┘
                               │
                         HTTP / REST API
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Django REST Backend │
                    │                     │
                    │ Mission Status      │
                    │ Robot Commands      │
                    │ Emergency Triage    │
                    │ Communication       │
                    └──────────┬──────────┘
                               │
                         Firebase Admin SDK
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Firebase Firestore  │
                    │                     │
                    │ mission             │
                    │ robot_commands      │
                    │ emergency_cases     │
                    │ communication_      │
                    │ actions             │
                    └─────────────────────┘