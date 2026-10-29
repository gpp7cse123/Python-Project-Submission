@echo off
title Python Quiz Application
echo Starting Python Quiz Application...
cd /d "%~dp0"
python main.py
if errorlevel 1 (
    echo.
    echo [ERROR] Application encountered an error or Python was not found in PATH.
    pause
)
