# NASA Space Apps Challenge 2026: Project Submission Pack
*Team Name: A3thr1X*  
*Challenge: Create Health Monitoring Software for Astronauts on Space Missions*  
*Ready to Copy & Paste directly into your NASA Space Apps "Project" tab.*

---

## 1. Project Name
```text
AstroPulse: Autonomous Deep-Space Crew Health Telemetry & Clinical Triage Cockpit
```

---

## 2. High-Level Project Summary
```text
On long-duration Artemis lunar and Mars exploration missions, communication latency with Earth ranges from 14 to 22 minutes each way. This delay makes real-time ground flight surgeon telemedicine impossible during acute physiological emergencies. Astronauts must take direct ownership of their health amidst microgravity fluid shifts, dangerous solar particle radiation storms, hostile closed cabin atmospheres, and sleep disruption.

We developed AstroPulse: a 100% offline-ready, edge-autonomous crew health cockpit and clinical decision engine. AstroPulse continuously ingests multi-modal biometrics (Lead II continuous ECG, arterial blood pressure, SpO2, core body temperature, circadian sleep cycles) alongside environmental sensors (ambient dosimeters and cabin CO2 levels). 

Grounding our algorithms in NASA Open Science Data Repository (OSDR) RadLab benchmarks and NASA Human Research Program clinical guidelines, AstroPulse autonomously triages spaceflight conditions—including Spaceflight-Associated Neuro-ocular Syndrome (SANS), Solar Particle Event (SPE) radiation surges, cabin hypercapnia, and cardiovascular deconditioning. When anomalies occur, AstroPulse delivers immediate, prioritized medical countermeasures (such as Lower Body Negative Pressure suit sessions, storm shelter evacuation, and life support scrubber overrides), ensuring crew health autonomy on the journey to deep space.
```

---

## 3. Link to Project Demo
```text
[INSERT PUBLIC GOOGLE DRIVE / SLIDESHARE / YOUTUBE LINK HERE]
Note: Must be either a 7-slide slide deck (see presentation/NASA_7Slide_Pitch.md) OR a 30-second or less demo video. Ensure link sharing is set to "Anyone with the link can view" with no password or login required.
```

---

## 4. Link to Final Project
```text
[INSERT PUBLIC GITHUB REPOSITORY LINK HERE - e.g. https://github.com/HariMuthuGanesh/AstroPulse-HealthMonitor]
```

---

## 5. Detailed Project Description

### What exactly does it do?
```text
AstroPulse provides astronauts with an autonomous, real-time medical cockpit designed for deep-space missions where communication delays prevent terrestrial medical assistance. It acts as an on-board flight surgeon assistant by:
1. Streaming and visualizing real-time biometrics (continuous ECG waveform, blood pressure, oxygen saturation, core body temperature, and circadian sleep metrics).
2. Tracking spaceflight environmental hazards (real-time ambient radiation flux in μSv/h and cabin CO2 levels in mmHg).
3. Running an autonomous clinical decision engine that monitors for spaceflight-specific syndromes, including Spaceflight-Associated Neuro-ocular Syndrome (SANS) cephalad fluid shifts, acute Solar Particle Event radiation spikes, hypoxia, and hypercapnia.
4. Providing actionable, non-pharmacological and clinical countermeasures with a streamlined acknowledgment workflow, enabling astronauts to resolve medical anomalies independently.
```

### How does it work?
```text
AstroPulse operates on an offline-first, dual-layer architecture:
- Edge Telemetry Daemon (Python / FastAPI): Runs locally on the spacecraft's internal server or avionics edge node. It ingests sensor streams, evaluates biometrics against NASA Human Research Program (HRP STD-3001) thresholds, and computes radiation risk metrics using historical NASA OSDR RadLab data.
- Mission Control Telemetry Cockpit (HTML5, Modern CSS, Vanilla JS): A low-cognitive-load heads-up display (HUD) that renders a real-time Lead II ECG oscilloscope canvas, vital metric gauges, environmental hazard trackers, and active clinical triage feeds.
- Offline Resilience: The frontend contains an embedded client-side fallback simulation engine. If the spacecraft server restarts or disconnects, the interface continues monitoring without losing telemetry fidelity or crashing.
```

### What benefits does it have?
```text
1. Eliminates Latency Risks: Empowers the crew to manage critical medical events instantly without waiting for a 20+ minute transmission roundtrip from Mission Control.
2. SANS & Vision Protection: Early detection of cephalad venous congestion prompts timely Lower Body Negative Pressure (LBNP) therapy to prevent irreversible optic nerve edema and choroidal folds.
3. Radiation Defense: Real-time dosimeter alerts warn astronauts of Solar Particle Events (SPEs), enabling rapid shelter evacuation before dangerous acute radiation doses are sustained.
4. Cognitive Load Reduction: Minimalist, mission-critical UI design prevents decision paralysis under high-stress conditions.
```

### What do you hope to achieve?
```text
Our objective is to deliver a reliable, flight-ready crew health telemetry framework that can be integrated into the Artemis Gateway and future crewed Mars transit vehicles, closing the telemedicine latency gap and keeping explorers healthy on multi-year interplanetary missions.
```

### What tools, coding languages, hardware, or software did you use?
```text
- Backend: Python 3.13, FastAPI, Uvicorn, WebSockets, Pydantic
- Frontend: HTML5, CSS3 (Glassmorphism Dark Space HUD), Vanilla JavaScript, Canvas API (real-time ECG oscilloscope)
- Datasets & Standards: NASA Open Science Data Repository (OSDR OSD-379 RadLab), NASA GeneLab (GL-EXP-202, GL-EXP-184), NASA Human Research Program Evidence Books & Standards (NASA-STD-3001)
- Version Control & Packaging: Git, GitHub, Batch automation
```

---

## 6. Use of Super Intelligence (SI)
```text
Yes. We utilized Large Language Models (LLMs) and agentic coding tools to accelerate codebase scaffolding, assist in synthesizing NASA Open Science Data Repository (OSDR) RadLab dosimetry benchmarks, and draft technical documentation. The core project concept, edge architecture design, physiological decision thresholds, and implementation were conceived and verified by team A3thr1X. All AI-assisted code has been reviewed for technical accuracy against NASA Human Research Program medical guidelines.
```

---

## 7. NASA Data
```text
1. NASA Open Science Data Repository (OSDR) - RadLab (Dataset OSD-379):
   Used to establish ionizing radiation dosimetry benchmarks across Low Earth Orbit (ISS Expedition 68), lunar translunar trajectories (Apollo 11 & Apollo 14), and deep-space cruise analogs (Mars Science Laboratory RAD detector data).

2. NASA GeneLab (GL-EXP-202, GL-EXP-184):
   Used biological stress marker references (gamma-H2AX histone phosphorylation for DNA double-strand breaks and 8-OHdG urinary oxidative stress metrics) to benchmark biological damage against radiation dosimeter thresholds.

3. NASA Human Research Program (HRP STD-3001 & Evidence Books):
   Clinical standards used to establish decision thresholds for Spaceflight-Associated Neuro-ocular Syndrome (SANS), cardiovascular deconditioning, cabin CO2 permissible limits (SSP 50005), and NCRP Report No. 132 career radiation exposure limits.
```

---

## 8. Space Agency Partner Data and Other References
```text
- European Space Agency (ESA): Bed rest analog studies on microgravity cephalad fluid shifts and Lower Body Negative Pressure (LBNP) countermeasure protocols.
- Canadian Space Agency (CSA): Astronaut cardiovascular deconditioning and vascular stiffness research in microgravity.
- JAXA (Japan Aerospace Exploration Agency): Circadian rhythm and sleep architecture metrics from Kibo module long-duration expeditions.
- National Council on Radiation Protection and Measurements (NCRP Report No. 132): Radiation career limits for astronauts.
```
