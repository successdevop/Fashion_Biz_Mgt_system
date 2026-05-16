from flask import jsonify
from demo import app
from demo.service.service import Services

class DemoController:
    def __init__(self, service: Services):
        self.service = service

    @app.route("/")
    def home(self):
        return jsonify({"message": "Welcome To Fashion Business Management System API"})

    @app.route("/users", methods=['GET'])
    def get_all_users(self):
        return self.service.get_users()

    @app.route("/countries", methods=['GET'])
    def get_all_countries(self):
        return self.service.get_countries()

    @app.route("/users/<int:user_id>", methods=['GET'])
    def get_a_user(self, user_id: int):
        return self.service.get_user(user_id)

    @app.route("/countries/<int:country_id>", methods=['GET'])
    def get_a_country(self, country_id: int):
        return self.service.get_country(country_id)

    @app.route("/users/<int:user_id>", methods=['DELETE'])
    def delete_user(self, user_id: int):
        return self.service.delete_user(user_id)

    @app.route("/countries/<int:country_id>", methods=['DELETE'])
    def delete_country(self, country_id: int):
        return self.service.delete_country(country_id)

    @app.route("/users/<int:user_id>", methods=['PATCH'])
    def update_user(self, user_id: int):
        return self.service.update_user(user_id)

    @app.route("/countries/<int:country_id>", methods=['PATCH'])
    def update_country(self, country_id: int):
        return self.service.update_country(country_id)

    @app.route("/users", methods=['POST'])
    def create_user(self):
        return self.service.create_user()

    @app.route("/countries", methods=['POST'])
    def add_country(self):
        return self.service.add_country()



