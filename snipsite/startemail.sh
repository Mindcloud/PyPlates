#!/bin/bash
PYTHONPATH=$PWD:$PWD/..${PYTHONPATH:+:$PYTHONPATH}
export PYTHONPATH

echo "** Starting Test Server **"
sudo python -m smtpd -n -cebuggingServer localhost:25

