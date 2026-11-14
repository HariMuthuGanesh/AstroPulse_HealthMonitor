"""
AstroPulse: NASA Space Apps Challenge 2026
FastAPI Backend & Autonomous Telemetry Service
"""

import json
import asyncio
from pathlib import Path
from typing import Dict, Any, List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .nasa_data import nasa_data_loader
from .clinical_engine import clinical_engine
from .telemetry_simulator import telemetry_simulator

BASE_DIR = Path(__file__).resolve().parent.parent
CREW_PATH = BASE_DIR / "datasets" / "crew_baseline.json"
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app = FastAPI(
    title="AstroPulse Crew Health System",
    description="Offline-First Autonomous Health Monitoring & Countermeasure Decision Support for Space Missions",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_crew() -> List[Dict[str, Any]]:
    if CREW_PATH.exists():
        with open(CREW_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

class ScenarioRequest(BaseModel):
    scenario: str

@app.get("/api/status")
def get_status():
    return {
        "system": "AstroPulse Autonomous Telemetry Core",
        "mission_mode": "Deep Space Transit (Mars / Artemis Lunar)",
        "offline_ready": True,
        "active_scenario": telemetry_simulator.scenario,
        "team": "A3thr1X",
        "challenge": "Create Health Monitoring Software for Astronauts on Space Missions"
    }

@app.get("/api/crew")
def get_crew():
    return load_crew()

@app.get("/api/telemetry/latest")
def get_latest_telemetry():
    crew = load_crew()
    results = []
    for member in crew:
        tel = telemetry_simulator.get_current_telemetry(member["id"], member["baseline"])
        eval_result = clinical_engine.evaluate_vitals(tel, member["baseline"])
        rad_eval = nasa_data_loader.evaluate_radiation_risk(
            tel["ambient_radiation_uSv_h"],
            member["baseline"]["cumulative_career_mSv"]
        )
        results.append({
            "astronaut": member,
            "telemetry": tel,
            "clinical_status": eval_result,
            "radiation_risk": rad_eval
        })
    return {
        "active_scenario": telemetry_simulator.scenario,
        "crew_telemetry": results
    }

@app.post("/api/telemetry/scenario")
def set_scenario(req: ScenarioRequest):
    success = telemetry_simulator.set_scenario(req.scenario)
    return {
        "success": success,
        "current_scenario": telemetry_simulator.scenario,
        "available_scenarios": telemetry_simulator.scenarios
    }

@app.get("/api/nasa-osdr")
def get_nasa_osdr_data():
    return {
        "benchmarks": nasa_data_loader.get_benchmarks(),
        "historical_missions": nasa_data_loader.get_historical_missions(),
        "biological_markers": nasa_data_loader.get_biological_markers()
    }

@app.websocket("/ws/telemetry")
async def websocket_telemetry(websocket: WebSocket):
    await websocket.accept()
    crew = load_crew()
    try:
        while True:
            payload = []
            for member in crew:
                tel = telemetry_simulator.get_current_telemetry(member["id"], member["baseline"])
                eval_result = clinical_engine.evaluate_vitals(tel, member["baseline"])
                payload.append({
                    "id": member["id"],
                    "callsign": member["callsign"],
                    "role": member["role"],
                    "telemetry": tel,
                    "clinical_status": eval_result
                })
            await websocket.send_json({
                "scenario": telemetry_simulator.scenario,
                "crew": payload
            })
            await asyncio.sleep(1.0)
    except WebSocketDisconnect:
        pass
    except Exception:
        pass

# Static Frontend mounting
if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

    @app.get("/")
    def serve_index():
        index_file = FRONTEND_DIR / "index.html"
        if index_file.exists():
            return FileResponse(str(index_file))
        return {"message": "Frontend index.html not found"}
