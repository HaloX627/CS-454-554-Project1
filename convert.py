# Create the application, let it read query parameters, and allow JSON responses
from flask import Flask, request, jsonify

# Use math to allow things like isFinite()
import math

# Create the app/server object
app = Flask(__name__)

# Define the endpoint. Only needs to respond to GET requests
@app.route("/convert", methods=["GET"])
def convert():

    # Get the 'lbs' query parameter from the URL
    lbs_param = request.args.get("lbs")

    # Check if parameter is missing or not a number
    try:
        lbs = float(lbs_param)

# If it is not, return a JSON 400 error
    except (TypeError, ValueError):
        return jsonify({"error": "Query param lbs is required and must be a number"}), 400

    # Check for invalid values (negative or non-finite)
    if not math.isfinite(lbs) or lbs < 0:
        return jsonify({"error": "lbs must be a non-negative, finite number"}), 422

    # Convert to kg, round to 3 decimals
    kg = round(lbs * 0.45359237, 3)

    return jsonify({
        "lbs": lbs,
        "kg": kg,
        "formula": "kg = lbs * 0.45359237"
    })

# Tell Flask to start the server
if __name__ == "__main__":
    # Run on all interfaces, port 8080
    app.run(host="0.0.0.0", port=8080)
