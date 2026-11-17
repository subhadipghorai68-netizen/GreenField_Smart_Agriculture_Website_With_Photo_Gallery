# GreenField Smart Agriculture Website

A beginner-friendly demo website built with Python Flask, HTML, CSS and JavaScript.

## Features
- Responsive farm dashboard
- Crop cards with field photographs
- Demo temperature, humidity, soil moisture and rain readings
- Demo irrigation on/off control (does NOT operate real equipment)
- Simple soil-moisture crop suggestion endpoint
- Photo URLs are loaded from Unsplash, so an internet connection is needed to display them

## Requirements
- Python 3.10 or newer
- Internet connection for first-time package installation and remote photos

## Run on Windows
1. Install Python from https://www.python.org/downloads/
2. During installation, tick **Add Python to PATH**.
3. Extract this ZIP file.
4. Open the extracted `smart_agriculture_website` folder.
5. In that folder, click the address bar, type `cmd`, and press Enter.
6. Run:
   `py -m venv .venv`
7. Activate the environment:
   `.venv\\Scripts\\activate`
8. Install Flask:
   `py -m pip install -r requirements.txt`
9. Start the website:
   `py app.py`
10. Open this address in your browser:
    http://127.0.0.1:5000
11. To stop the server, return to Command Prompt and press Ctrl+C.

## Run on macOS / Linux
1. Install Python 3.10+.
2. Open Terminal and move into the extracted project folder using `cd`.
3. Create an environment:
   `python3 -m venv .venv`
4. Activate it:
   `source .venv/bin/activate`
5. Install dependencies:
   `python -m pip install -r requirements.txt`
6. Start:
   `python app.py`
7. Open http://127.0.0.1:5000 in your browser.
8. Stop with Ctrl+C.

## Customize
- Edit sample readings and farm name in `app.py`.
- Edit crop names and image URLs in `templates/index.html`.
- Change colors and layout in `static/css/style.css`.
- Add browser interactions in `static/js/main.js`.

## Important
This is a learning/demo project. Sensor values and weather are sample values, not live data.
The irrigation button only changes demo status in the website. It is not connected to a pump,
relay, microcontroller, or farm equipment. Crop suggestions are basic examples, not professional
agronomic advice. For a real deployment, use authenticated APIs, validated sensor data,
secure hardware controls, and local agricultural guidance.
