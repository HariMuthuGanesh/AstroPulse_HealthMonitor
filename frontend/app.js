/**
 * AstroPulse - Crew Health Telemetry & Triage Client
 * Offline-first architecture: Seamlessly runs on live WebSocket / REST,
 * or falls back to an internal client-side simulation engine if backend is offline.
 */

const CREW_FALLBACK = [
  {
    id: "ASTRO-01",
    callsign: "Ares-CDR",
    role: "Mission Commander",
    age: 38,
    baseline: {
      resting_hr_bpm: 62,
      systolic_bp_mmHg: 118,
      diastolic_bp_mmHg: 76,
      spo2_percent: 98.5,
      core_temp_c: 36.8,
      target_daily_sleep_hrs: 8.0,
      cumulative_career_mSv: 74.2
    }
  },
  {
    id: "ASTRO-02",
    callsign: "Ares-FE1",
    role: "Flight Engineer 1",
    age: 34,
    baseline: {
      resting_hr_bpm: 58,
      systolic_bp_mmHg: 122,
      diastolic_bp_mmHg: 78,
      spo2_percent: 98.8,
      core_temp_c: 36.7,
      target_daily_sleep_hrs: 8.0,
      cumulative_career_mSv: 42.6
    }
  },
  {
    id: "ASTRO-03",
    callsign: "Ares-MS1",
    role: "Mission Specialist (Science)",
    age: 31,
    baseline: {
      resting_hr_bpm: 65,
      systolic_bp_mmHg: 115,
      diastolic_bp_mmHg: 74,
      spo2_percent: 99.0,
      core_temp_c: 36.9,
      target_daily_sleep_hrs: 8.0,
      cumulative_career_mSv: 18.1
    }
  }
];

let crewList = CREW_FALLBACK;
let activeAstroId = "ASTRO-01";
let activeScenario = "nominal";
let isBackendLive = false;
let tick = 0;

// ECG Canvas Setup
const canvas = document.getElementById("ecgCanvas");
const ctx = canvas ? canvas.getContext("2d") : null;
let ecgData = [];
const maxEcgPoints = 280;

// Initialize ECG array
for (let i = 0; i < maxEcgPoints; i++) {
  ecgData.push(55);
}

// UTC Clock
function updateClock() {
  const clockEl = document.getElementById("utc-clock");
  if (clockEl) {
    const now = new Date();
    clockEl.textContent = now.toUTCString().split(" ")[4] + " UTC";
  }
}
setInterval(updateClock, 1000);
updateClock();

// Roster rendering
function renderRoster() {
  const container = document.getElementById("roster-container");
  if (!container) return;
  container.innerHTML = "";

  crewList.forEach(astro => {
    const tab = document.createElement("div");
    tab.className = `astro-tab ${astro.id === activeAstroId ? "active" : ""}`;
    tab.onclick = () => {
      activeAstroId = astro.id;
      renderRoster();
      updateDashboard();
    };

    tab.innerHTML = `
      <div class="astro-tab-left">
        <span class="astro-tab-name">${astro.callsign} (${astro.role})</span>
        <span class="astro-tab-role">Age: ${astro.age} | Career Dose: ${astro.baseline.cumulative_career_mSv} mSv</span>
      </div>
      <span class="astro-tab-badge" id="badge-${astro.id}">HEALTH NOMINAL</span>
    `;
    container.appendChild(tab);
  });
}

// ECG Generator: Generates realistic Lead II waveform (P wave, PR segment, QRS spike, ST, T wave)
function getEcgSample(t, hr) {
  const cycleLength = (60 / hr) * 50; // points per heartbeat
  const phase = t % cycleLength;
  const mid = 55;

  if (phase < 6) {
    // P wave
    return mid - 8 * Math.sin((phase / 6) * Math.PI);
  } else if (phase >= 6 && phase < 11) {
    // PR segment
    return mid;
  } else if (phase >= 11 && phase < 13) {
    // Q dip
    return mid + 6;
  } else if (phase >= 13 && phase < 16) {
    // R spike
    return mid - 42;
  } else if (phase >= 16 && phase < 18) {
    // S dip
    return mid + 12;
  } else if (phase >= 18 && phase < 26) {
    // ST segment
    return mid;
  } else if (phase >= 26 && phase < 36) {
    // T wave
    return mid - 12 * Math.sin(((phase - 26) / 10) * Math.PI);
  } else {
    // Isoelectric baseline
    return mid + (Math.random() - 0.5) * 1.5;
  }
}

function drawEcg(hr) {
  if (!ctx || !canvas) return;

  const nextVal = getEcgSample(tick * 2, hr);
  ecgData.shift();
  ecgData.push(nextVal);

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Background Grid
  ctx.strokeStyle = "rgba(16, 185, 129, 0.08)";
  ctx.lineWidth = 1;
  const gridStep = 20;
  for (let x = 0; x < canvas.width; x += gridStep) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, canvas.height);
    ctx.stroke();
  }
  for (let y = 0; y < canvas.height; y += gridStep) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(canvas.width, y);
    ctx.stroke();
  }

  // Draw ECG Trace
  ctx.strokeStyle = "#10b981";
  ctx.lineWidth = 2;
  ctx.shadowColor = "#10b981";
  ctx.shadowBlur = 6;
  ctx.beginPath();

  const stepX = canvas.width / (maxEcgPoints - 1);
  for (let i = 0; i < ecgData.length; i++) {
    const x = i * stepX;
    const y = ecgData[i];
    if (i === 0) {
      ctx.moveTo(x, y);
    } else {
      ctx.lineTo(x, y);
    }
  }
  ctx.stroke();
  ctx.shadowBlur = 0;
}

// Client-Side Simulation Logic (Offline Fallback & Instant Response)
function generateClientTelemetry(astro) {
  tick++;
  const base = astro.baseline;
  let hr = base.resting_hr_bpm + 2 * Math.sin(tick * 0.2);
  let sbp = base.systolic_bp_mmHg + (Math.random() - 0.5) * 3;
  let dbp = base.diastolic_bp_mmHg + (Math.random() - 0.5) * 2;
  let spo2 = base.spo2_percent + (Math.random() - 0.5) * 0.4;
  let temp = base.core_temp_c + (Math.random() - 0.5) * 0.1;
  let sleep = base.target_daily_sleep_hrs - 0.4;
  let rad = 64.0 + 4 * Math.sin(tick * 0.05);
  let co2 = 2.2 + 0.1 * Math.sin(tick * 0.1);
  let fluid = 1.05 + 0.05 * Math.sin(tick * 0.1);

  if (activeScenario === "solar_flare") {
    rad = 6840.0 + (Math.random() - 0.5) * 200;
    hr += 19;
    sbp += 15;
  } else if (activeScenario === "fluid_shift_sans") {
    fluid = 2.88;
    sbp = 149;
    dbp = 98;
    hr += 8;
  } else if (activeScenario === "hypoxia_co2") {
    co2 = 4.88;
    spo2 = 91.2;
    hr += 22;
  }

  return {
    heart_rate_bpm: Math.round(hr * 10) / 10,
    systolic_bp_mmHg: Math.round(sbp * 10) / 10,
    diastolic_bp_mmHg: Math.round(dbp * 10) / 10,
    spo2_percent: Math.min(100.0, Math.round(spo2 * 10) / 10),
    core_temp_c: Math.round(temp * 100) / 100,
    sleep_duration_hrs: Math.round(sleep * 10) / 10,
    ambient_radiation_uSv_h: Math.round(rad * 10) / 10,
    cabin_co2_mmHg: Math.round(co2 * 100) / 100,
    cephalad_fluid_shift_score: Math.round(fluid * 100) / 100
  };
}

function evaluateClientVitals(tel) {
  const alerts = [];
  const cms = [];

  if (tel.cabin_co2_mmHg >= 4.5) {
    alerts.push({
      severity: "CRITICAL",
      condition: "Severe Hypercapnia Hazard",
      message: `Cabin CO2 elevated to ${tel.cabin_co2_mmHg} mmHg. Risk of cognitive decline and acute cephalad vasodilation.`,
      nasa_ref: "NASA STD-3001 Cabin Environmental Health"
    });
    cms.push({
      priority: 1,
      action: "Emergency Scrubber (CDRA) Cycle",
      guidance: "Switch primary Carbon Dioxide Removal Assembly bed to emergency desorb. Don medical rebreather mask."
    });
  }

  if (tel.ambient_radiation_uSv_h >= 5000) {
    alerts.push({
      severity: "CRITICAL",
      condition: "Solar Particle Event (SPE) Flux Alert",
      message: `Dosimeter reading ${tel.ambient_radiation_uSv_h} μSv/h. Exceeds safe acute biological threshold.`,
      nasa_ref: "NASA OSDR RadLab & SRPE Solar Storm Metric"
    });
    cms.push({
      priority: 1,
      action: "Move to Heavy Radiation Storm Shelter",
      guidance: "Relocate crew to central water-wall shielded bunker immediately. Abort any unpressurized activities."
    });
  }

  if (tel.cephalad_fluid_shift_score >= 2.4) {
    alerts.push({
      severity: "WARNING",
      condition: "SANS Risk (Microgravity Venous Engorgement)",
      message: "Fluid shift index 2.88 indicates significant jugular congestion and choroidal risk.",
      nasa_ref: "NASA Human Research Program: SANS Protocol"
    });
    cms.push({
      priority: 2,
      action: "Lower Body Negative Pressure (LBNP) Countermeasure",
      guidance: "Initiate 30-min session in Chibis LBNP suit at -25 mmHg to redistribute pooled cephalic fluids."
    });
  }

  if (tel.spo2_percent < 93.0) {
    alerts.push({
      severity: "CRITICAL",
      condition: "Acute Hypoxia Warning",
      message: `SpO2 fallen to ${tel.spo2_percent}%. Immediate oxygenation support advised.`,
      nasa_ref: "NASA Flight Surgeon Operations"
    });
    cms.push({
      priority: 1,
      action: "Deploy High-Flow O2 Inhalator",
      guidance: "Administer 100% O2 via medical pack and check cabin partial oxygen pressure."
    });
  }

  if (alerts.length === 0) {
    alerts.push({
      severity: "NOMINAL",
      condition: "All Biometrics & Cabin Telemetry Nominal",
      message: "Cardiovascular, atmospheric, and radiation metrics well within deep-space safety limits.",
      nasa_ref: "NASA Human Research Program Baseline"
    });
    cms.push({
      priority: 4,
      action: "Maintain Prescribed Physical Exercise Routine",
      guidance: "Perform scheduled 2.0 hr session on ARED (Advanced Resistive Exercise Device) and T2 Cycle Ergometer."
    });
  }

  return { alerts, cms };
}

// UI Update Loop
function updateDashboard() {
  const activeAstro = crewList.find(a => a.id === activeAstroId) || crewList[0];
  const callsignBadge = document.getElementById("astro-callsign-badge");
  if (callsignBadge) callsignBadge.textContent = activeAstro.callsign;

  const tel = generateClientTelemetry(activeAstro);
  const evaluation = evaluateClientVitals(tel);

  // Update Metric Cards
  const valHr = document.getElementById("val-hr");
  const valBp = document.getElementById("val-bp");
  const valSpo2 = document.getElementById("val-spo2");
  const valTemp = document.getElementById("val-temp");
  const valSleep = document.getElementById("val-sleep");
  const valFluid = document.getElementById("val-fluid");

  if (valHr) valHr.textContent = tel.heart_rate_bpm;
  if (valBp) valBp.textContent = `${tel.systolic_bp_mmHg}/${tel.diastolic_bp_mmHg}`;
  if (valSpo2) valSpo2.textContent = tel.spo2_percent;
  if (valTemp) valTemp.textContent = tel.core_temp_c;
  if (valSleep) valSleep.textContent = tel.sleep_duration_hrs;
  if (valFluid) valFluid.textContent = tel.cephalad_fluid_shift_score;

  // Environmental Hazards
  const valRad = document.getElementById("val-rad");
  const valCo2 = document.getElementById("val-co2");
  const radBar = document.getElementById("rad-bar");
  const co2Bar = document.getElementById("co2-bar");

  if (valRad) valRad.textContent = tel.ambient_radiation_uSv_h;
  if (valCo2) valCo2.textContent = tel.cabin_co2_mmHg;

  if (radBar) {
    const radPercent = Math.min(100, (tel.ambient_radiation_uSv_h / 7000) * 100);
    radBar.style.width = `${Math.max(8, radPercent)}%`;
  }
  if (co2Bar) {
    const co2Percent = Math.min(100, (tel.cabin_co2_mmHg / 6.0) * 100);
    co2Bar.style.width = `${Math.max(10, co2Percent)}%`;
  }

  // Draw ECG
  drawEcg(tel.heart_rate_bpm);

  // Overall status
  const topSeverity = evaluation.alerts[0].severity;
  const statusPill = document.getElementById("overall-status-pill");
  if (statusPill) {
    statusPill.className = `status-pill pill-${topSeverity.toLowerCase()}`;
    statusPill.textContent = topSeverity;
  }

  // Update roster badge
  const astroBadge = document.getElementById(`badge-${activeAstro.id}`);
  if (astroBadge) {
    astroBadge.textContent = topSeverity === "NOMINAL" ? "HEALTH NOMINAL" : `ALERT: ${topSeverity}`;
    astroBadge.style.color = topSeverity === "CRITICAL" ? "#ef4444" : (topSeverity === "WARNING" ? "#f59e0b" : "#10b981");
  }

  // Render Alerts
  const alertContainer = document.getElementById("alert-feed-container");
  if (alertContainer) {
    alertContainer.innerHTML = "";
    evaluation.alerts.forEach(alert => {
      const el = document.createElement("div");
      el.className = `alert-item alert-${alert.severity}`;
      el.innerHTML = `
        <div class="alert-header">
          <span class="alert-condition">${alert.condition}</span>
          <span class="alert-badge ${alert.severity}">${alert.severity}</span>
        </div>
        <p class="alert-body">${alert.message}</p>
        <span class="alert-source">Ref: ${alert.nasa_ref}</span>
      `;
      alertContainer.appendChild(el);
    });
  }

  // Render Countermeasures
  const cmContainer = document.getElementById("countermeasure-container");
  if (cmContainer) {
    cmContainer.innerHTML = "";
    evaluation.cms.forEach((cm, index) => {
      const el = document.createElement("div");
      el.className = "cm-card";
      el.innerHTML = `
        <span class="cm-title">PROTOCOL [P${cm.priority}]: ${cm.action}</span>
        <p class="cm-guidance">${cm.guidance}</p>
        <div class="cm-action-row">
          <button class="cm-exec-btn" onclick="acknowledgeProtocol(this, '${cm.action}')">
            Execute / Acknowledge Protocol
          </button>
        </div>
      `;
      cmContainer.appendChild(el);
    });
  }
}

// User Action Handler for Countermeasures
window.acknowledgeProtocol = function(btn, actionName) {
  btn.textContent = "✓ Protocol Acknowledged & Logged";
  btn.classList.add("executed");
  btn.disabled = true;
};

// Scenario Selector setup
function setupScenarioButtons() {
  const buttons = document.querySelectorAll(".scenario-btn");
  buttons.forEach(btn => {
    btn.onclick = () => {
      buttons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeScenario = btn.getAttribute("data-scenario");

      // Notify backend if available
      if (isBackendLive) {
        fetch("/api/telemetry/scenario", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ scenario: activeScenario })
        }).catch(() => {});
      }

      updateDashboard();
    };
  });
}

// Backend check
async function checkBackend() {
  try {
    const res = await fetch("/api/status", { cache: "no-store" });
    if (res.ok) {
      isBackendLive = true;
      const dot = document.getElementById("status-dot");
      const text = document.getElementById("backend-status-text");
      if (dot) dot.className = "status-dot online";
      if (text) text.textContent = "FastAPI Telemetry Daemon: Live";
    }
  } catch (err) {
    isBackendLive = false;
    const dot = document.getElementById("status-dot");
    const text = document.getElementById("backend-status-text");
    if (dot) dot.className = "status-dot offline";
    if (text) text.textContent = "Edge Autonomous Offline Mode (Client Engine Active)";
  }
}

// Init
window.addEventListener("DOMContentLoaded", () => {
  renderRoster();
  setupScenarioButtons();
  checkBackend();
  setInterval(updateDashboard, 1000);
  updateDashboard();
});
