#!/bin/bash

echo "Installing pip Packages"
pip install -r requirements.txt

echo "Collecting Static Files"
python3 manage.py collectstatic --noinput