#!/usr/bin/env bash

set -ex

PYTHON="${PYTHON:-python3}"
which ${PYTHON} > /dev/null
if [ $? -ne 0 ]; then
    PYTHON=python
fi

MAJOR=$(${PYTHON} -c 'import sys; print(sys.version_info.major)')
MINOR=$(${PYTHON} -c 'import sys; print(sys.version_info.minor)')
echo "${PYTHON} v${MAJOR}.${MINOR}"
if [ ${MAJOR} -eq 3 ] && [ ${MINOR} -lt 10 ] || [ ${MAJOR} -lt 3 ]; then
    echo "${PYTHON} version must at least be 3.10" >&2
    exit 1
fi

${PYTHON} -m pip install --progress-bar off --upgrade -r requirements.txt

if python -c 'import torch;assert torch.__version__.startswith("2.0.")' &>/dev/null 2>&1; then
    PYTORCH=$(python -c 'import torch;print(torch.__version__)')
    echo "pytorch available: ${PYTORCH}"
else
    if [ ! $CI = "true" ] && command -v conda &>/dev/null 2>&1; then
        conda install -y pytorch==2.0.0
    else
        ${PYTHON} -m pip install --progress-bar off torch==2.0.0
    fi
    echo "installed pytorch. it's probably better if you install it yourself"
fi
