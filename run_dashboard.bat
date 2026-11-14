@echo off
echo ============================================================
echo   ASTROPULSE - NASA SPACE APPS CHALLENGE 2026
echo   Autonomous Deep-Space Crew Health Telemetry & Triage
echo   Team: A3thr1X
echo ============================================================
echo.
cd /d "%~dp0"

echo [1/2] Starting AstroPulse FastAPI Telemetry Daemon...
start /b python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000

echo [2/2] Opening Mission Control Telemetry Cockpit in Browser...
timeout /t 2 >nul
start http://127.0.0.1:8000/

echo.
echo Dashboard is running at http://127.0.0.1:8000/
echo To open offline directly, double click frontend/index.html
echo Press Ctrl+C in this console to terminate the server.
echo.
cmd /k
