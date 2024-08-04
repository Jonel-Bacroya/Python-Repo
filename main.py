from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/get-user-details/<user_id>")
def get_user_details(user_id):
    user_details = {
        "username":"jonelbacroya",
        "emailaddress": "test_emailaddress@yahoo.com",
        "notes":"likes spicy food"
    }

    if user_id:
        return jsonify(user_details), 200
    else:
        return "invalid user", 404

@app.route("/create-user", methods=["Post"])
def create_user():
    user_details = request.get_json()

    if user_details:
        user_details["created"] = "success!"
        return jsonify(user_details),201
    else:
        return "failed to create!",404
    
if __name__ == "__main__":
    app.run(debug=True)