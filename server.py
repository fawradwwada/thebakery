from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_cookie', methods=['POST'])
def receive_cookie():
    data = request.get_json()

    # Log received cookie (educational use only)
    print("Received data:", data)

    return jsonify({"status": "success", "message": "Cookie received"})
