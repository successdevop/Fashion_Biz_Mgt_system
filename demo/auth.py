from flask import request, jsonify
from demo import auth, app
from demo.models.user import UserModel
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token


@auth.verify_password
def verify_password(email, password):
    user = UserModel.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user
    return None

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"message":"Invalid or missing json"}), 400

    email = data.get("email")
    password = data.get("password")

    user = UserModel.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message":"Invalid email or password"}), False

    access_token = create_access_token(identity=email)
    return jsonify({"message":"login successful",
                    "access_token":access_token,
                    "token_type":"Bearer"
                    }), 200