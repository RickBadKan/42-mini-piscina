#!/bin/bash

FREEZE_PIP="$(python3 -m pip freeze)"

if [[ "$FREEZE_PIP" == *"virtualenv"* ]]; then
    python3 -m virtualenv --clear venv_d04
    source "./venv_d04/bin/activate"
    pip install -r requirements.txt
else
    python3 -m pip install virtualenv
    source "./create_venv.sh"
fi