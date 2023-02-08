#!/bin/bash

pip -V

PATH_INSTALATION_PIP="$(pip freeze --path ./local_lib)"

if [[ "$PATH_INSTALATION_PIP" == *"path"* ]]; then
    pip install path -t ./local_lib/ --upgrade >./install.log
else
    pip install path -t ./local_lib/ >./install.log
fi

python3 ./my_program.py
