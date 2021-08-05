#!/bin/bash
python3 manage.py dummy_data
python3 manage.py migrate --no-input

