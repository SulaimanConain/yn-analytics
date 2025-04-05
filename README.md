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

## License

Copyright © 2024 YN-ANALYTICS. All rights reserved. 
