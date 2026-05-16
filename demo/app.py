# from flask import Flask, jsonify
# from flask_marshmallow import Marshmallow
# from .repository.repo import db
#
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fashion_biz.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db.init_app(app)
# ma = Marshmallow(app)
#
#
# from demo.models.country import CountryModel
# from demo.models.user import UserModel
# from demo.service.service import Services
#
# service = Services(db)
# @app.route("/")
# def home():
#     return jsonify({"message": "Welcome To Fashion Business Management System API"})
#
# @app.route("/users", methods=['GET'])
# def get_all_users(self):
#     return self.service.get_users()
#
# @app.route("/countries", methods=['GET'])
# def get_all_countries(self):
#     return self.service.get_countries()
#
# @app.route("/users/<int:user_id>", methods=['GET'])
# def get_a_user(self, user_id: int):
#     return self.service.get_user(user_id)
#
# @app.route("/countries/<int:country_id>", methods=['GET'])
# def get_a_country(self, country_id: int):
#     return self.service.get_country(country_id)
#
# @app.route("/users/<int:user_id>", methods=['DELETE'])
# def delete_user(self, user_id: int):
#     return self.service.delete_user(user_id)
#
# @app.route("/countries/<int:country_id>", methods=['DELETE'])
# def delete_country(self, country_id: int):
#     return self.service.delete_country(country_id)
#
# @app.route("/users/<int:user_id>", methods=['PATCH'])
# def update_user(self, user_id: int):
#     return self.service.update_user(user_id)
#
# @app.route("/countries/<int:country_id>", methods=['PATCH'])
# def update_country(self, country_id: int):
#     return self.service.update_country(country_id)
#
# @app.route("/users", methods=['POST'])
# def create_user(self):
#     return self.service.create_user()
#
# @app.route("/countries", methods=['POST'])
# def add_country(self):
#     return self.service.add_country()
#
#
# @app.cli.command("create_db")
# def create_db():
#     db.create_all()
#     print("DATABASE created")
#
#
# @app.cli.command("drop_db")
# def drop_db():
#     db.drop_all()
#     print("DATABASE dropped")
#
#
# @app.cli.command("db_seed")
# def db_seed():
#     usa = CountryModel(country_name="Nigeria", country_capital="Abuja", country_population=200000349)
#     user = UserModel(first_name="Success", last_name="Raphael", email="successraphael28@gmail.com",
#                      password="password")
#
#     db.session.add(usa)
#     db.session.add(user)
#     db.session.commit()
#
#     print("DATABASE seeded")
#
#
# if __name__ == "__main__":
#     app.run()
#
#
from demo import app

if __name__ == "__main__":
    app.run()