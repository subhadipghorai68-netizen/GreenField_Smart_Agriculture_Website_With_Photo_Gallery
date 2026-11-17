from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Demo data: replace these values with real sensor/API data when available.
FARM = {
    "farm_name": "GreenField Smart Farm",
    "location": "Your Farm",
    "temperature": 28,
    "humidity": 64,
    "soil_moisture": 42,
    "rain_chance": 25,
    "ph": 6.5,
    "crop": "Rice",
}

@app.route("/")
def home():
    return render_template("index.html", farm=FARM)

@app.route("/api/irrigation", methods=["POST"])
def irrigation():
    data = request.get_json(silent=True) or {}
    action = data.get("action")
    if action not in ("on", "off"):
        return jsonify({"ok": False, "message": "Invalid irrigation action."}), 400
    # This is a demonstration only. It does not control a real pump.
    return jsonify({
        "ok": True,
        "status": "ON" if action == "on" else "OFF",
        "message": f"Demo irrigation switched {action.upper()}. No physical equipment was controlled."
    })

@app.route("/api/advice", methods=["POST"])
def advice():
    data = request.get_json(silent=True) or {}
    crop = (data.get("crop") or "your crop").strip()[:40]
    moisture = data.get("moisture", FARM["soil_moisture"])
    try:
        moisture = float(moisture)
    except (TypeError, ValueError):
        return jsonify({"advice": "Please enter a valid soil-moisture value."}), 400

    if moisture < 30:
        advice_text = f"Soil moisture is low. Check the soil near the roots and consider watering {crop} if the crop's growth stage and local conditions require it."
    elif moisture > 75:
        advice_text = "Soil moisture is high. Check drainage and avoid adding water until the field has been assessed."
    else:
        advice_text = f"Soil moisture is in a moderate demo range. Keep monitoring {crop} and follow local agricultural guidance."
    return jsonify({"advice": advice_text})

if __name__ == "__main__":
    app.run(debug=True)
