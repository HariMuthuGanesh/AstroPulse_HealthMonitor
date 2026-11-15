# AstroPulse: 7-Slide Pitch Presentation Guide
*Format: NASA Space Apps Challenge 2026 strict limit: Maximum 7 slides (including title and intro).*

---

## Slide 1: Title & Team Introduction (Mandatory)
* **Title**: **AstroPulse // Autonomous Deep-Space Health Telemetry & Triage Cockpit**
* **Challenge**: Create Health Monitoring Software for Astronauts on Space Missions
* **Team Name**: **A3thr1X**
* **Institution**: National Engineering College
* **Team Members**:
  - Hari Muthu Ganesh R (Team Lead & Systems Architecture)
  - Syed Sufyan M (Biometric Data Engineering & ML Models)
  - Afzal Ali K A H (Frontend Cockpit & Human Factors UX)
* **Visual**: AstroPulse mission patch icon with Deep Space Orion / Mars transit backdrop.

---

## Slide 2: The Critical Deep-Space Problem
* **The Challenge**: Deep-space transit (Artemis Lunar / Mars missions) introduces a 14 to 22-minute one-way communication delay with Earth Mission Control.
* **The Medical Reality**:
  - Earth telemedicine and ground flight surgeons cannot intervene in real-time acute medical emergencies.
  - Microgravity triggers Spaceflight-Associated Neuro-ocular Syndrome (SANS) via cephalad fluid shifts.
  - Space radiation (Galactic Cosmic Rays & Solar Particle Events) threatens acute cellular degradation.
  - Hostile closed cabin environments cause atmospheric CO2 spikes and circadian fatigue.
* **The Core Need**: Astronauts require a 100% offline, edge-autonomous health monitoring system that detects early biometric decline and gives immediate actionable clinical protocols.

---

## Slide 3: The Solution — AstroPulse OS Architecture
* **What We Developed**: An edge-native crew health operating system operating entirely disconnected from Earth.
* **System Breakdown**:
  1. **Multi-Modal Telemetry Ingestion**: Continuous 100 Hz ECG, SpO2, arterial blood pressure, core temperature, and cabin atmosphere sensors.
  2. **Autonomous Clinical Decision Engine**: Algorithmic triage based on NASA Human Research Program clinical practice guidelines.
  3. **Real-Time Hazard Alerting**: Instant detection of acute solar radiation storms, SANS fluid congestion, hypercapnia, and cardiac stress.
  4. **Actionable Countermeasures Engine**: Step-by-step non-pharmacological protocols (LBNP suits, oxygen scrubbers, rehydration, storm shelters).

---

## Slide 4: NASA Open Data Grounding & Space Agency Integration
* **NASA OSDR RadLab (Dataset OSD-379)**:
  - Integrated historical dosimetry benchmarks (Apollo 11, Apollo 14, ISS Expedition 68, and Mars Science Laboratory RAD detector data).
  - Career radiation budget tracking against NASA NCRP 132 career limits (600 mSv ceiling).
* **NASA GeneLab Biomarkers**:
  - Biological stress indicators (gamma-H2AX DNA double-strand breaks and 8-OHdG oxidative stress markers) mapped to radiation thresholds.
* **NASA Human Research Program (HRP STD-3001)**:
  - NASA spaceflight medical standards integrated directly into our rule-based triage thresholds.

---

## Slide 5: The Astronaut User Experience & Cockpit Demo
* **Low Cognitive Load Design**:
  - Mission-critical dark HUD designed for high-stress, zero-g cabin conditions.
  - At-a-glance status pills (NOMINAL, WARNING, CRITICAL) preventing information overload.
* **Interactive Cockpit Features**:
  - Lead II live ECG oscilloscope canvas.
  - Dual Environmental Hazard monitors (Ambient Radiation Flux μSv/h and Cabin CO2 mmHg).
  - Multi-crew roster switching (Commander, Flight Engineer, Science Specialist).
  - One-click "Execute / Acknowledge Protocol" workflow for crew compliance.
* **Visual**: Screenshot of the AstroPulse Telemetry Cockpit running live scenarios.

---

## Slide 6: Verification & Stress Scenarios
* **Demonstrated Resilience Under 4 Operational Scenarios**:
  1. **Nominal Cruise**: Routine cardiovascular and circadian tracking with ARED/T2 exercise schedules.
  2. **Solar Particle Event (SPE)**: Flux spike >6,500 μSv/h triggers instant evacuation protocol to the central water-wall shielded bunker.
  3. **SANS Cephalad Fluid Shift**: Elevated jugular venous score triggers immediate Lower Body Negative Pressure (LBNP) decompression session.
  4. **Life Support Scrubber Drop**: Cabin CO2 climb to 4.8 mmHg triggers emergency CDRA bed regeneration and supplemental O2 guidance.
* **Offline First Resilience**: Seamless operation on edge hardware with zero reliance on cloud servers or Earth internet.

---

## Slide 7: Impact & The Road to Artemis & Mars
* **Immediate Value**:
  - Eliminates the dangerous operational blind spot caused by Earth communication latency.
  - Protects astronaut vision, organ health, and mission success on multi-year exploration class missions.
* **Extensibility & Future Scope**:
  - Integration with Artemis gateway wearable biosensors and Orion cabin avionics.
  - Terrestrial spin-off: Remote telemetry triage for Antarctic research stations, offshore maritime platforms, and rural disaster zones without internet connectivity.
* **Final Tagline**: *AstroPulse: Autonomous medical intelligence for humanity's journey to the stars.*
