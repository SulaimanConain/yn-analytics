# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Start Gunicorn server
gunicorn --bind 0.0.0.0:5000 --workers 4 wsgi:app 