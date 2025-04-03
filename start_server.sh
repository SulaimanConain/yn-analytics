#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Start Gunicorn server
gunicorn --bind 0.0.0.0:5000 --workers 4 wsgi:app 