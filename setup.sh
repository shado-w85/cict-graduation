#!/usr/bin/env bash
# setup.sh - creates the virtual environment on macOS / Linux.
# Run:  bash setup.sh
set -e
cd "$(dirname "$0")"

echo "1/4  Creating virtual environment in ./venv ..."
python3 -m venv venv

echo "2/4  Activating it ..."
source venv/bin/activate

echo "3/4  Upgrading pip and installing requirements ..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "4/4  Building the attendee list ..."
python scripts/make_list.py

echo ""
echo "Setup complete."
echo "To use the project later, run:  source venv/bin/activate"
