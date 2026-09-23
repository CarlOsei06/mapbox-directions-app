# Mapbox Directions App

A simple navigation web application that allows users to enter an origin and destination, then displays a route on an interactive Mapbox map. The backend is powered by Flask and uses Mapbox's Geocoding and Directions APIs to compute routes and coordinates.

---

## 🚀 Features

- Interactive Mapbox GL JS map
- Search for origin and destination
- Flask backend for geocoding + routing
- Draws the full route polyline on the map
- Adds markers for start and end points
- Automatically fits the map to the route bounds

---

## 🗂 Project Structure
project/
│
├── static/
│   └── script.js        # Frontend logic + Mapbox map
│
├── templates/
│   └── index.html       # UI layout
│
├── app.py               # Flask backend (routing + geocoding)
├── requirements.txt     # Python dependencies
└── .gitignore           # Ignore secrets + environment files

Code

---

## ⚙️ Backend (Flask)

GET /directions?origin=<text>&destination=<text>

Code

It returns:

- Origin coordinates  
- Destination coordinates  
- Full route geometry  
- Mapbox Directions API response  

---

## 🎨 Frontend (Mapbox GL JS)

The frontend:

- Loads the Mapbox map  
- Sends user input to the backend  
- Draws the route  
- Adds markers  
- Fits the map to the route  

---

The backend exposes a single endpoint:
