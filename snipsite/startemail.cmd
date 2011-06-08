#!/bin/bash
PYTHONPATH=$PWD:$PWD/..${PYTHONPATH:+:$PYTHONPATH}
export PYTHONPATH

echo "** Starting Test Server **"
python -m smtpd -n -c DebuggingServer localhost:25

