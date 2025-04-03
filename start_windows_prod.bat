@echo off
call venv\Scripts\activate.bat
python -m waitress --listen=0.0.0.0:5000 wsgi:app 