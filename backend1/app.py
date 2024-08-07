from flask import Flask, request, jsonify

app = Flask(__name__)

users = { 
    "user1" : {"username": "root", "password": "Nitin@123"}
}

def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"The credentials are not right "}), 400
    user = users.get(username)

    if not username or not user["password"] != password:
        return jsonify({"error": "invalid username or password"}), 401
    return jsonify ({"message": "Login succesful", "user": user}), 200

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = "8000")



