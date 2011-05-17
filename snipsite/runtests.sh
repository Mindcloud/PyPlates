#!/bin/bash
PYTHONPATH=$PWD:$PWD/..${PYTHONPATH:+:$PYTHONPATH}
export PYTHONPATH

echo "** Running basic API test **"
python manage.py test mysite
