"""
Autonomous Clinical Decision Engine for Spaceflight Physiology
Based on NASA Human Research Program (HRP) Evidence Books:
- SANS (Spaceflight-Associated Neuro-ocular Syndrome)
- Space Radiation Carcinogenesis & Acute Dosimetry
- Cardiovascular Deconditioning & Orthostatic Intolerance
- Hostile Closed Cabin Atmosphere (CO2 / Hypoxia)
- Behavioral Health & Circadian Disruption
"""

from typing import Dict, Any, List

class ClinicalDecisionEngine:
    """
    Evaluates real-time biometric and cabin environmental telemetry to produce
    prioritized triage alerts and actionable non-pharmacological / medical countermeasures.
    """

    def evaluate_vitals(self, telemetry: Dict[str, Any], baseline: Dict[str, Any]) -> Dict[str, Any]:
        alerts: List[Dict[str, Any]] = []
        countermeasures: List[Dict[str, Any]] = []

        hr = telemetry.get("heart_rate_bpm", 72)
        sbp = telemetry.get("systolic_bp_mmHg", 120)
        dbp = telemetry.get("diastolic_bp_mmHg", 80)
        spo2 = telemetry.get("spo2_percent", 98.0)
        core_temp = telemetry.get("core_temp_c", 36.8)
        sleep_hrs = telemetry.get("sleep_duration_hrs", 7.5)
        radiation_rate = telemetry.get("ambient_radiation_uSv_h", 65.0)
        cabin_co2 = telemetry.get("cabin_co2_mmHg", 2.1) # Earth normal: ~0.3 mmHg, ISS nominal: 2-3 mmHg, Caution: >3.8 mmHg
        fluid_shift_index = telemetry.get("cephalad_fluid_shift_score", 1.0) # 1.0 nominal, 2.5+ elevated SANS risk

        pulse_pressure = sbp - dbp

        # 1. Atmospheric CO2 & Hypoxia Triage
        if cabin_co2 >= 4.5:
            alerts.append({
                "severity": "CRITICAL",
                "condition": "Severe Hypercapnia Hazard",
                "message": f"Cabin CO2 elevated to {cabin_co2} mmHg. Impairs decision making, causes intracranial vasodilation.",
                "nasa_ref": "NASA HRP Closed Environment Standard (SSP 50005)"
            })
            countermeasures.append({
                "priority": 1,
                "action": "Atmospheric Life Support Scrubber Override",
                "guidance": "Cycle CDRA (Carbon Dioxide Removal Assembly) to emergency bed regeneration. Don temporary O2 mask if symptomatic."
            })
        elif cabin_co2 >= 3.8:
            alerts.append({
                "severity": "WARNING",
                "condition": "Elevated Ambient CO2",
                "message": f"Cabin CO2 at {cabin_co2} mmHg (approaching symptomatic ceiling).",
                "nasa_ref": "NASA HRP Closed Environment Standard"
            })
            countermeasures.append({
                "priority": 3,
                "action": "Increase Local Cabin Air Circulation",
                "guidance": "Verify ventilation fans in crew quarters; avoid stagnant CO2 pockets."
            })

        if spo2 < 93.0:
            alerts.append({
                "severity": "CRITICAL",
                "condition": "Acute Hypoxemia",
                "message": f"Blood oxygen saturation fallen to {spo2}%. Immediate hypoxic risk.",
                "nasa_ref": "Space Flight Medical Operations"
            })
            countermeasures.append({
                "priority": 1,
                "action": "Supplementary Oxygen Protocol",
                "guidance": "Verify suit/cabin partial pressure. Inhale 100% O2 via crew medical kit mask."
            })

        # 2. SANS (Spaceflight-Associated Neuro-ocular Syndrome) & Fluid Shift
        if fluid_shift_index >= 2.4 or (sbp >= 145 and dbp >= 95):
            alerts.append({
                "severity": "WARNING",
                "condition": "Elevated SANS Risk (Cephalad Venous Engorgement)",
                "message": "Fluid shift score elevated; increased jugular venous distension and potential choroidal fold risk.",
                "nasa_ref": "NASA SANS Clinical Practice Guideline"
            })
            countermeasures.append({
                "priority": 2,
                "action": "Chazos LBNP (Lower Body Negative Pressure) Protocol",
                "guidance": "Undergo 30 minutes of -25 mmHg LBNP session to draw pooled blood back toward lower limbs."
            })

        # 3. Radiation Spike / Solar Storm (SPE)
        if radiation_rate >= 5000.0: # >5 mSv/hr
            alerts.append({
                "severity": "CRITICAL",
                "condition": "Solar Particle Event (SPE) Radiation Storm",
                "message": f"Radiation flux at {radiation_rate} uSv/h. Acute radiation syndrome risk.",
                "nasa_ref": "NASA Space Radiation Program Element (SRPE)"
            })
            countermeasures.append({
                "priority": 1,
                "action": "Crew Quarters Storm Shelter Protocol",
                "guidance": "Immediately abort EVA / station activities. Relocate to polyethylene/water-shielded center core."
            })
        elif radiation_rate >= 150.0:
            alerts.append({
                "severity": "WARNING",
                "condition": "Elevated Cosmic Radiation Dosage",
                "message": f"Ambient flux at {radiation_rate} uSv/h. Exceeds nominal deep space background.",
                "nasa_ref": "NASA OSDR RadLab Baseline"
            })

        # 4. Cardiovascular Strain & Orthostatic Intolerance
        if hr > 115 and pulse_pressure < 25:
            alerts.append({
                "severity": "WARNING",
                "condition": "Cardiovascular Deconditioning / Tachycardia",
                "message": f"Heart rate elevated ({hr} BPM) with narrow pulse pressure ({pulse_pressure} mmHg).",
                "nasa_ref": "NASA Cardiovascular Risk Stand"
            })
            countermeasures.append({
                "priority": 2,
                "action": "Fluid Loading & Rehydration",
                "guidance": "Consume 1.0 L electrolyte isotonic solution (AstroLyte salt tablets) prior to strenuous tasks."
            })

        # 5. Circadian Sleep Deficit & Neurobehavioral Fatigue
        if sleep_hrs < 5.0:
            alerts.append({
                "severity": "WARNING",
                "condition": "Acute Sleep Deprivation",
                "message": f"Only {sleep_hrs} hours logged. Elevated risk for reaction time slowdown and procedural error.",
                "nasa_ref": "NASA Behavioral Health and Performance (BHP)"
            })
            countermeasures.append({
                "priority": 3,
                "action": "Circadian Light Phase Shift & Workload Throttle",
                "guidance": "Schedule 45-minute power nap in shielded bunk; switch cabin lighting to 480nm blue-depleted warm light."
            })

        # Default Nominal state
        if not alerts:
            alerts.append({
                "severity": "NOMINAL",
                "condition": "All Biometrics Nominal",
                "message": "All cardiovascular, atmospheric, and radiation telemetry within safe spaceflight limits.",
                "nasa_ref": "NASA HRP Standards 3001"
            })
            countermeasures.append({
                "priority": 4,
                "action": "Maintain Routine Countermeasure Regimen",
                "guidance": "Complete scheduled 2.5 hour T2 Treadmill and ARED (Advanced Resistive Exercise Device) workout."
            })

        # Sort alerts: CRITICAL first, then WARNING, then NOMINAL
        severity_rank = {"CRITICAL": 0, "WARNING": 1, "NOMINAL": 2}
        alerts.sort(key=lambda a: severity_rank.get(a["severity"], 3))
        countermeasures.sort(key=lambda c: c["priority"])

        overall_status = alerts[0]["severity"]

        return {
            "overall_status": overall_status,
            "alerts": alerts,
            "countermeasures": countermeasures
        }

clinical_engine = ClinicalDecisionEngine()
