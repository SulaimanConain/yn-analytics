# YN-ANALYTICS Web Application

A modern, responsive Flask web application for YN-ANALYTICS energy management services.

## Features

- Modern black and white theme with professional design
- Responsive layout that works on all devices
- Interactive elements (FAQ accordions, smooth scrolling, form validation)
- Mapbox integration for location visualization
- Contact form with validation

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Libraries**: FontAwesome (icons), Mapbox GL JS (maps)
- **Fonts**: Inter (Google Fonts)

## Project Structure

```
yn-analytics/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/             # Static assets
│   ├── css/            # CSS stylesheets
│   ├── js/             # JavaScript files
│   └── img/            # Images
└── templates/          # HTML templates
    └── index.html      # Main HTML file
```

## Setup Instructions

1. **Clone the repository**
   ```
   git clone https://github.com/SulaimanConain/yn-analytics.git
   cd yn-analytics
   ```

2. **Create a virtual environment**
   ```
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```
   python app.py
   ```

5. **Access the website**
   ```
   Open your browser and navigate to http://127.0.0.1:5000/
   ```

## Customization

To customize the application:

- Update the content in `templates/index.html`
- Modify styles in `static/css/style.css`
- Add your Mapbox API key in `static/js/main.js`
- Add your own images to `static/img/`

## Production Deployment

For production deployment:

1. Set the appropriate environment variables

2. **On Linux/Unix systems:**
   Use Gunicorn to serve the application:
   ```
   # Make the script executable first
   chmod +x start_server.sh
   ./start_server.sh
   ```
   Or run Gunicorn directly:
   ```
   gunicorn --bind 0.0.0.0:5000 --workers 4 wsgi:app
   ```

3. **On Windows systems:**
   Use Waitress (a production-ready WSGI server for Windows):
   ```
   # Install Waitress if not already installed
   pip install waitress
   
   # Run with Waitress
   .\start_windows_prod.ps1
   ```
   Or run directly with:
   ```
   python -m waitress --listen=0.0.0.0:5000 wsgi:app
   ```
   
   Alternatively, for development purposes:
   ```
   .\start_windows.ps1
   ```

4. Set up a reverse proxy with Nginx or Apache

5. Consider containerizing with Docker

## License

Copyright © 2024 YN-ANALYTICS. All rights reserved. 