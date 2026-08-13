from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Flask CI/CD Application is running",
        "status": "success"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/api/status")
def status():
    return jsonify({
        "application": "Flask CI/CD Demo",
        "status": "running"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)