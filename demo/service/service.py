from flask import jsonify, request

from demo.models.country import CountryModel
from demo.models.user import UserModel
from demo.schemas.country import countries_schema, country_schema
from demo.schemas.user import users_schema, user_schema


class Services:
    def __init__(self, database):
        self.db = database

    def delete_user(self, user_id: int):
        user = UserModel.query.filter_by(user_id=user_id).first()
        if not user:
            return jsonify({"message":"user not found"}), 404

        self.db.session.delete(user)
        self.db.session.commit()

        return jsonify({"message": f"user with id {user_id} deleted"}), 202


    def delete_country(self, country_id: int):
        country = CountryModel.query.filter_by(user_id=country_id).first()
        if not country:
            return jsonify({"message":"country not found"}), 404

        self.db.session.delete(country)
        self.db.session.commit()

        return jsonify({"message": f"country with id {country_id} deleted"}), 202


    def update_user(self, user_id: int):
        user = UserModel.query.get(user_id)
        if not user:
            return jsonify({"message":"user not found"}), 404

        data = request.get_json()
        if "first_name" in data:
            user.first_name = data['first_name']
        if "last_name" in data:
            user.last_name = data['last_name']
        if "email" in data:
            user.email = data['email']
        if "password" in data:
            user.password = data['password']

        self.db.session.commit()

        return jsonify({"message":f"user with id {user_id} updated successfully"}), 201


    def update_country(self, user_id: int):
        country = CountryModel.query.get(user_id)
        if not country:
            return jsonify({"message":"country not found"}), 404

        data = request.get_json()
        if "country_name" in data:
            country.first_name = data['country_name']
        if "country_capital" in data:
            country.last_name = data['country_capital']
        if "country_population" in data:
            country.email = data['country_population']

        self.db.session.commit()

        return jsonify({"message":f"country with id {user_id} updated successfully"}), 201


    def create_user(self):
        try:
            if request.is_json:
                data = request.get_json()
                first_name = data.get("first_name")
                last_name = data.get("last_name")
                email = data.get("email")
                password = data.get("password")
            else:
                first_name = request.form.get("first_name")
                last_name = request.form.get("last_name")
                email = request.form.get("email")
                password = request.form.get("password")

            if UserModel.query.filter_by(email=email).first():
                return jsonify({"message":"user already exists"})

            new_user = UserModel(first_name=first_name, last_name=last_name, email=email, password=password)
            self.db.session.add(new_user)
            self.db.commit()

            return jsonify({"message":"user created successfully"}), 201
        except Exception as e:
            self.db.rollback()
            print(f"Error occurred | {e}]")


    def add_country(self):
        try:
            if request.is_json:
                data = request.get_json()
                country_name = data.get("country_name")
                country_capital = data.get("country_capital")
                country_population = data.get("country_population")
            else:
                country_name = request.form.get("country_name")
                country_capital = request.form.get("country_capital")
                country_population = request.form.get("country_population")

            if CountryModel.query.filter_by(country_name=country_name).first():
                return jsonify({"message":"country already exists"})

            new_country = CountryModel(country_name=country_name, country_capital=country_capital,
                                       country_population=country_population)
            self.db.session.add(new_country)
            self.db.commit()

            return jsonify({"message":"country created successfully"}), 201
        except Exception as e:
            self.db.rollback()
            print(f"Error occurred | {e}]")


    @staticmethod
    def get_countries():
        countries = CountryModel.query.all()
        if not countries:
            return jsonify({"message":"No countries found"}), 404

        return jsonify(countries_schema.dump(countries)), 200


    @staticmethod
    def get_users():
        users = UserModel.query.all()
        if not users:
            return jsonify(({"message":"No users found"})), 404

        return jsonify(users_schema.dump(users)), 200


    @staticmethod
    def get_user(user_id: int):
        user = UserModel.query.get(user_id)
        if not user:
            return jsonify({"Error":f"user with id {user_id} not found"}), 404

        return jsonify(user_schema.dump(user)), 200


    @staticmethod
    def get_country(country_id: int):
        country = CountryModel.query.get(country_id)
        if not country:
            return jsonify(({"error":f"country with id {country_id} not found"})), 404

        return jsonify(country_schema.dump(country)), 200








