"""
NASA Data Loader & Dosimetry Risk Engine
Ingests NASA Open Science Data Repository (OSDR) RadLab and GeneLab benchmarks.
Evaluates radiation exposures against NASA Human Research Program thresholds.
"""

import json
from pathlib import Path
from typing import Dict, Any, List

DATASET_PATH = Path(__file__).resolve().parent.parent / "datasets" / "nasa_osdr_radiation.json"

class NasaDataLoader:
    def __init__(self):
        self._data: Dict[str, Any] = {}
        self.load()

    def load(self):
        if DATASET_PATH.exists():
            with open(DATASET_PATH, "r", encoding="utf-8") as f:
                self._data = json.load(f)
        else:
            self._data = {}

    def get_benchmarks(self) -> Dict[str, Any]:
        return self._data.get("reference_benchmarks", {})

    def get_historical_missions(self) -> List[Dict[str, Any]]:
        return self._data.get("historical_mission_samples", [])

    def get_biological_markers(self) -> List[Dict[str, Any]]:
        return self._data.get("biological_stress_markers", [])

    def evaluate_radiation_risk(self, current_rate_uSv_h: float, career_cumulative_mSv: float) -> Dict[str, Any]:
        """
        Assesses acute solar particle event (SPE) rate and cumulative career limits
        per NASA NCRP Report No. 132 and Human Research Program guidelines.
        """
        benchmarks = self.get_benchmarks()
        spe_threshold_uSv_h = 5000.0  # 5 mSv/hr = 5000 uSv/hr dangerous acute rate
        warning_rate_uSv_h = 100.0    # 0.1 mSv/hr = elevated galactic cosmic ray flux
        career_limit = benchmarks.get("nasa_career_limit_mSv", 600.0)

        remaining_career_budget = max(0.0, career_limit - career_cumulative_mSv)
        percent_career_used = (career_cumulative_mSv / career_limit) * 100.0

        if current_rate_uSv_h >= spe_threshold_uSv_h:
            status = "CRITICAL_SOLAR_PARTICLE_EVENT"
            recommendation = "Immediate crew evacuation to heavy storm shelter. Deploy water-wall radiation shields."
        elif current_rate_uSv_h >= warning_rate_uSv_h:
            status = "ELEVATED_COSMIC_FLUX"
            recommendation = "Minimize EVA (spacewalk) duration. Monitor dosimeter real-time rate."
        else:
            status = "NOMINAL_DEEP_SPACE"
            recommendation = "Background radiation within expected deep space envelope."

        return {
            "status": status,
            "current_rate_uSv_h": round(current_rate_uSv_h, 2),
            "career_cumulative_mSv": round(career_cumulative_mSv, 2),
            "career_limit_mSv": career_limit,
            "career_budget_remaining_mSv": round(remaining_career_budget, 2),
            "percent_career_used": round(percent_career_used, 1),
            "recommendation": recommendation,
            "nasa_osdr_reference": "NASA OSDR OSD-379 RadLab / MSL RAD"
        }

nasa_data_loader = NasaDataLoader()
