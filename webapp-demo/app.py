# Basic Flask server
# - Create a Flask app
# - GET "/" should render templates/index.html
# - GET "/api/hello" should return JSON: {"message": "Hello from Flask!"}
# - Run with debug=True when executed directly
from flask import Flask, render_template, jsonify   
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/hello")
def hello():
    return jsonify(message="Hello from Flask! Working.........")

# Add: /api/time route to return ISO timestamp
@app.route("/api/time")
def api_time():
    now = datetime.datetime.now(datetime.timezone.utc)
    return jsonify(timestamp=now.isoformat())

if __name__ == "__main__":
    app.run(debug=True)
