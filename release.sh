#!/bin/bash
python3 manage.py migrate --no-input
python3 manage.py dummy_data

