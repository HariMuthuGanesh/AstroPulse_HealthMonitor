"""
Real-Time Crew Health Telemetry Simulator
Generates time-series biometric and cabin telemetry for the crew.
Supports switching simulation scenarios on the fly.
"""

import math
import random
import time
from typing import Dict, Any, List

class TelemetrySimulator:
    def __init__(self):
        self.scenario = "nominal"
        self.tick_count = 0
        self.scenarios = ["nominal", "solar_flare", "fluid_shift_sans", "hypoxia_co2"]

    def set_scenario(self, scenario_name: str) -> bool:
        if scenario_name in self.scenarios:
            self.scenario = scenario_name
            return True
        return False

    def get_current_telemetry(self, astro_id: str, baseline: Dict[str, Any]) -> Dict[str, Any]:
        self.tick_count += 1
        t = self.tick_count

        # Base nominal vitals with minor sinus arrhythmia fluctuation
        base_hr = baseline.get("resting_hr_bpm", 64)
        base_sbp = baseline.get("systolic_bp_mmHg", 118)
        base_dbp = baseline.get("diastolic_bp_mmHg", 76)
        base_spo2 = baseline.get("spo2_percent", 98.5)
        base_temp = baseline.get("core_temp_c", 36.8)

        hr_jitter = 2.0 * math.sin(t * 0.2) + random.uniform(-1.5, 1.5)
        hr = base_hr + hr_jitter
        sbp = base_sbp + random.uniform(-2, 2)
        dbp = base_dbp + random.uniform(-1.5, 1.5)
        spo2 = base_spo2 + random.uniform(-0.3, 0.3)
        temp = base_temp + random.uniform(-0.1, 0.1)
        sleep_hrs = baseline.get("target_daily_sleep_hrs", 7.8) - 0.4
        radiation_rate = 62.0 + 5.0 * math.sin(t * 0.05) + random.uniform(-3, 3) # uSv/h nominal deep space
        cabin_co2 = 2.2 + 0.2 * math.sin(t * 0.1) # mmHg ISS baseline
        fluid_shift = 1.05 + 0.1 * math.sin(t * 0.1)

        # Apply Scenario Overrides
        if self.scenario == "solar_flare":
            # Solar Particle Event (SPE)
            radiation_rate = 6800.0 + random.uniform(-150, 250) # >6.8 mSv/hr
            hr += 18 # stress response
            sbp += 14

        elif self.scenario == "fluid_shift_sans":
            # SANS cephalad congestion
            fluid_shift = 2.85 + random.uniform(-0.1, 0.2)
            sbp = 148 + random.uniform(-3, 3)
            dbp = 98 + random.uniform(-2, 2)
            hr += 8

        elif self.scenario == "hypoxia_co2":
            # Life support scrubber failure
            cabin_co2 = 4.85 + random.uniform(-0.2, 0.3) # hazardous hypercapnia
            spo2 = 91.5 + random.uniform(-0.5, 0.5)
            hr += 24
            sbp += 10

        return {
            "astronaut_id": astro_id,
            "scenario": self.scenario,
            "timestamp": time.time(),
            "heart_rate_bpm": round(hr, 1),
            "systolic_bp_mmHg": round(sbp, 1),
            "diastolic_bp_mmHg": round(dbp, 1),
            "pulse_pressure_mmHg": round(sbp - dbp, 1),
            "spo2_percent": round(min(100.0, spo2), 1),
            "core_temp_c": round(temp, 2),
            "sleep_duration_hrs": round(sleep_hrs, 1),
            "ambient_radiation_uSv_h": round(radiation_rate, 1),
            "cabin_co2_mmHg": round(cabin_co2, 2),
            "cephalad_fluid_shift_score": round(fluid_shift, 2)
        }

telemetry_simulator = TelemetrySimulator()
