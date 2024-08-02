from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user-details/<user_id>")
def get_user_details(user_id):
    user_detail = {
        "user_id": user_id,
        "user_name": "Jonel-Bacroya",
        "email_address": "test_email_add@yahoo.com.ph"
    }

    additional_details = request.args.get("details")

    if additional_details:
        user_detail["additional_details"] = additional_details

    return jsonify(user_detail), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    # this part should point to a database entity to save 
    # the posted information
    user_details = request.get_json()

    return jsonify(user_details), 201



if __name__ == "__main__":
    app.run(debug=True)

