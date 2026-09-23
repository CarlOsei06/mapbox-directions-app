import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv

# Get the absolute path to the directory containing app.py
basedir = os.path.abspath(os.path.dirname(__file__))

# Explicitly load the .env file from this exact directory
load_dotenv(os.path.join(basedir, ".env"))

MAPBOX_ACCESS_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN")
print("Loaded token:", MAPBOX_ACCESS_TOKEN)

app = Flask(__name__)

@app.route("/directions")
def directions():
    origin = request.args.get("origin")
    destination = request.args.get("destination")

    # Convert origin/destination into coordinates using Mapbox Geocoding API
    geocode_url = "https://api.mapbox.com/geocoding/v5/mapbox.places/{place}.json?access_token={token}"

    def geocode(place):
        url = geocode_url.format(place=place, token=MAPBOX_ACCESS_TOKEN)
        response = requests.get(url).json()

        # Safety check
        if "features" not in response or len(response["features"]) == 0:
            print("Geocoding failed:", response)
            return None

        return response["features"][0]["center"]

    origin_coords = geocode(origin)
    destination_coords = geocode(destination)

    # If geocoding failed, return an error instead of crashing
    if origin_coords is None or destination_coords is None:
        return jsonify({
            "error": "Could not geocode one or both locations.",
            "token_loaded": MAPBOX_ACCESS_TOKEN is not None
        }), 400

    # Build Directions API request
    directions_url = (
        f"https://api.mapbox.com/directions/v5/mapbox/driving/"
        f"{origin_coords[0]},{origin_coords[1]};"
        f"{destination_coords[0]},{destination_coords[1]}"
        f"?geometries=geojson&access_token={MAPBOX_ACCESS_TOKEN}"
    )

    directions_response = requests.get(directions_url).json()

    return jsonify({
        "origin": origin,
        "destination": destination,
        "origin_coords": origin_coords,
        "destination_coords": destination_coords,
        "route": directions_response,
        "token_loaded": MAPBOX_ACCESS_TOKEN is not None
    })

app.run(debug=True)
