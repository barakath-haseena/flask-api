from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify({user_id: users[user_id]}), 200
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    user_id = len(users) + 1
    users[user_id] = data["name"]
    return jsonify({"message": "User created", "id": user_id}), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    users[user_id] = data["name"]
    return jsonify({"message": "User updated"}), 200

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)