from flask import Flask, jsonify, request

app = Flask(__name__)


SUPPORTED_ISSUE_TYPES = [
    "PASSWORD_RESET",
    "VPN_ACCESS",
    "WIFI_ISSUE",
    "SOFTWARE_ISSUE",
    "HARDWARE_ISSUE",
    "ACCOUNT_ACCESS",
    "GENERAL_QUERY"
]


@app.route("/")
def home():
    return jsonify({
        "message": "AI IT Support Automation Assistant API is running"
    })


@app.route("/support/request", methods=["POST"])
def create_support_request():
    data = request.get_json()

    name = data.get("name")
    issue_type = data.get("issue_type")
    description = data.get("description")
    priority = data.get("priority")

    # Check whether required information is provided
    if not name or not issue_type or not description or not priority:
        return jsonify({
            "status": "error",
            "message": "Missing required information"
        }), 400

    # Check whether the issue type is supported
    if issue_type not in SUPPORTED_ISSUE_TYPES:
        return jsonify({
            "status": "error",
            "message": "Unsupported issue type",
            "supported_issue_types": SUPPORTED_ISSUE_TYPES
        }), 400

    return jsonify({
        "status": "success",
        "message": "IT support request received",
        "request": {
            "name": name,
            "issue_type": issue_type,
            "description": description,
            "priority": priority
        }
    }), 201


if __name__ == "__main__":
    app.run(debug=True)