from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_cookie', methods=['POST'])
def receive_cookie():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        cookie_value = data.get("cookie")

        if cookie_value:
            # You can print the cookie to console or save it to a database
            print(f"Received Cookie: {cookie_value}")
            return jsonify({"message": "Cookie received successfully!"}), 200
        else:
            return jsonify({"message": "Cookie not provided!"}), 400
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
