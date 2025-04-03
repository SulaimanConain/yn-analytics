# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Start Flask development server with production settings
$env:FLASK_ENV = "production"
python app.py 