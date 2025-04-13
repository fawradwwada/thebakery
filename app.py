from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_cookie', methods=['POST'])
def receive_cookie():
    data = request.get_json()
    cookie = data.get('cookie', None)
    if cookie:
        # WARNING: Avoid exposing sensitive data in production.
        app.logger.info("Received cookie: %s", cookie)
        return jsonify({"message": "Cookie received successfully.", "cookie": cookie}), 200
    else:
        return jsonify({"error": "No cookie provided."}), 400

if __name__ == '__main__':
    # For Railway, listen on all interfaces. Railway sets the PORT env var.
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
