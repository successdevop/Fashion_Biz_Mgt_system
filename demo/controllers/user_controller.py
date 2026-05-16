from flask import jsonify
from demo import app
from demo.service.service import Services
from demo import db


service = Services(database=db)
@app.route("/")
def home():
    return jsonify({"message": "Welcome To Fashion Business Management System API"})

@app.route("/users", methods=['GET'])
def get_all_users():
    return service.get_users()

@app.route("/countries", methods=['GET'])
def get_all_countries():
    return service.get_countries()

@app.route("/users/<int:user_id>", methods=['GET'])
def get_a_user(user_id: int):
    return service.get_user(user_id)

@app.route("/countries/<int:country_id>", methods=['GET'])
def get_a_country(country_id: int):
    return service.get_country(country_id)

@app.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id: int):
    return service.delete_user(user_id)

@app.route("/countries/<int:country_id>", methods=['DELETE'])
def delete_country(country_id: int):
    return service.delete_country(country_id)

@app.route("/users/<int:user_id>", methods=['PATCH'])
def update_user(user_id: int):
    return service.update_user(user_id)

@app.route("/countries/<int:country_id>", methods=['PATCH'])
def update_country(country_id: int):
    return service.update_country(country_id)

@app.route("/users", methods=['POST'])
def create_user():
    return service.create_user()

@app.route("/countries", methods=['POST'])
def add_country():
    return service.add_country()



