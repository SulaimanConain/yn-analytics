# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Start Waitress WSGI server
python -m waitress --listen=0.0.0.0:5000 wsgi:app 