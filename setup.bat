@echo off
REM setup.bat - creates the virtual environment on Windows.
REM Run by double-clicking, or in Command Prompt:  setup.bat
cd /d "%~dp0"

echo 1/4  Creating virtual environment in .\venv ...
python -m venv venv
if errorlevel 1 goto :error

echo 2/4  Activating it ...
call venv\Scripts\activate.bat

echo 3/4  Upgrading pip and installing requirements ...
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 goto :error

echo 4/4  Building the attendee list ...
python scripts\make_list.py

echo.
echo Setup complete.
echo To use the project later, run:  venv\Scripts\activate
pause
exit /b 0

:error
echo.
echo Something went wrong. Check that Python is installed (python --version).
pause
exit /b 1
