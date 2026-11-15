# 🚀 AstroPulse // Autonomous Deep-Space Health Telemetry & Triage Cockpit

**NASA Space Apps Challenge 2026**  
**Challenge**: *Create Health Monitoring Software for Astronauts on Space Missions*  
**Team**: **A3thr1X** (Hari Muthu Ganesh R, Syed Sufyan M, Afzal Ali K A H)  
**Institution**: National Engineering College

---

## 📌 Problem Overview
Deep-space missions to the Moon (Artemis) and Mars introduce an Earth-space communication latency of 14 to 22 minutes one-way. In medical emergencies, real-time ground flight surgeon telemedicine is impossible. Astronauts face:
- **Microgravity fluid shifts** causing Spaceflight-Associated Neuro-ocular Syndrome (SANS) and intracranial pressure elevation.
- **Space radiation** (Solar Particle Events & Galactic Cosmic Rays) causing cellular and DNA damage.
- **Hostile closed atmospheres** with elevated ambient CO2 (>3.8 mmHg causing cognitive slowdown).
- **Circadian disruption** and sleep debt leading to procedural errors.

## 💡 The Solution: AstroPulse
AstroPulse is a 100% offline-ready, edge-native health monitoring cockpit and autonomous clinical decision support system:
1. **Multi-Modal Biometrics**: Continuous Lead II ECG waveform, blood pressure, SpO2, core body temperature, and circadian sleep logs.
2. **Environmental Hazard Monitors**: Ambient radiation dosimeter (μSv/h) grounded in NASA OSDR RadLab benchmarks, and cabin CO2 monitoring.
3. **Autonomous Clinical Decision Engine**: Algorithmic triage based on NASA Human Research Program (HRP STD-3001) clinical guidelines.
4. **Actionable Countermeasures**: Immediate guidance protocols (Lower Body Negative Pressure suits, storm shelter relocation, scrubber overrides) with an acknowledgment workflow.
5. **Offline-First Architecture**: Operates with a local FastAPI daemon or 100% standalone inside the browser via an embedded simulation engine.

---

## 📂 Project Structure
```text
D:\hackathon\AstroPulse-HealthMonitor\
├── README.md                           # Complete project documentation
├── NASA_SUBMISSION_PACK.md             # Copy-paste text for the NASA Project tab
├── run_dashboard.bat                   # One-click launch script
├── presentation/
│   └── NASA_7Slide_Pitch.md            # Compliant 7-slide pitch deck structure
├── backend/
│   ├── requirements.txt                # Python dependencies (FastAPI, Uvicorn, WebSockets)
│   ├── app/
│   │   ├── main.py                     # FastAPI server, REST & WebSocket routes
│   │   ├── clinical_engine.py          # NASA HRP clinical decision triage logic
│   │   ├── nasa_data.py                # NASA OSDR RadLab & GeneLab loader
│   │   └── telemetry_simulator.py      # Real-time multi-scenario biometric stream
│   └── datasets/
│       ├── nasa_osdr_radiation.json    # Real NASA OSDR RadLab radiation benchmarks
│       └── crew_baseline.json          # Astronaut baseline profiles
└── frontend/
    ├── index.html                      # Dark Mission Control Telemetry Cockpit
    ├── style.css                       # Space HUD styling & glassmorphism
    └── app.js                          # Real-time ECG generator & telemetry renderer
```

---

## 🛠️ How to Run

### Method 1: One-Click Runner (Recommended)
Double-click `run_dashboard.bat`. This starts the local FastAPI server and opens `http://127.0.0.1:8000/` in your default browser.

### Method 2: Manual Terminal
```powershell
cd D:\hackathon\AstroPulse-HealthMonitor
python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```
Then open `http://127.0.0.1:8000/` in your browser.

### Method 3: 100% Standalone Offline (No Python Required)
Simply double-click `frontend/index.html`. The built-in client engine runs all scenarios and ECG simulations locally.

---

## 🛰️ NASA Data Grounding
- **NASA Open Science Data Repository (OSDR) RadLab (OSD-379)**: Radiation benchmarks across Apollo 11/14, ISS Expedition 68, and Mars Science Laboratory RAD detector measurements.
- **NASA GeneLab (GL-EXP-202, GL-EXP-184)**: DNA double-strand break markers (gamma-H2AX foci) and oxidative stress metrics (8-OHdG).
- **NASA Human Research Program (NASA-STD-3001)**: Clinical thresholds for SANS, hypercapnia, and orthostatic deconditioning.
