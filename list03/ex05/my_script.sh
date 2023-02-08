#!/bin/bash

FREEZE_PIP="$(python3 -m pip freeze)"

if [[ "$FREEZE_PIP" == *"virtualenv"* ]]; then
    python3 -m virtualenv --clear django_venv
    source "./django_venv/bin/activate"
    pip install -r requirement.txt
else
    python3 -m pip install virtualenv
    source "./my_script.sh"
fi
