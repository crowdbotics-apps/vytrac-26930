#!/bin/bash
echo "Running release commands"
python3 manage.py dummy_data
echo $?
echo "test message"
python3 manage.py migrate --no-input

