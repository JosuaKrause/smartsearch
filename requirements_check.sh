#!/usr/bin/env bash

PYTHON="${PYTHON:-python3}"
FILE=${1:-requirements.txt}

${PYTHON} -m pip freeze | sort -sf | grep -i -E "^($(cat ${FILE} | sed -E 's/[=~]=.+//' | perl -p -e 'chomp if eof' | tr '\n' '|'))=" | diff -U 0 ${FILE} -

echo "NOTE: '+' is your local version and '-' is the version in ${FILE}" 1>&2
