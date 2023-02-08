#!/bin/bash

# A requirement.txt file that must include the latest stable versions of django and
# psycopg2.
#   A script with the following behavior:
#   Have the .sh extension.
#   Create a virtualenv on python3 named django_venv.
#   Install the requirement.txt file that you’ve created in the VirtualEnv.
#   The virtualenv must be activated when quitting.

FREEZE_PIP="$(python3 -m pip freeze)"

if [[ "$FREEZE_PIP" == *"virtualenv"* ]]; then
    python3 -m virtualenv --clear django_venv
    source "./django_venv/bin/activate"
    pip install -r requirement.txt
else
    python3 -m pip install virtualenv
    source "./my_script.sh"
fi
