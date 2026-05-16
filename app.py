# from flask import Flask, jsonify, request
# from sqlalchemy import Column, Integer, String, Float
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
# ma = Marshmallow(app)
#
# class User(db.Model):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     email = Column(String, unique=True)
#     password = Column(String)
#
# class Country(db.Model):
#     __tablename__ = "countries"
#     country_id = Column(Integer, primary_key=True)
#     country_name = Column(String)
#     country_capital = Column(String)
#     area = Column(Float)
#
# class UserSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = User
#         fields = ("id", "first_name", "last_name", "email", "password")
#
# class CountrySchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Country
#         fields = ("country_id", "country_name", "country_capital", "area")
#
# user_schema = UserSchema()
# users_schema = UserSchema(many=True)
#
# country_schema = CountrySchema()
# countries_schema = CountrySchema(many=True)
#
#
# @app.cli.command("db_create")
# def db_create():
#     db.create_all()
#     print("Database created")
#
#
# @app.cli.command("db_drop")
# def db_drop():
#     db.drop_all()
#     print("Database dropped")
#
#
# @app.cli.command("db_seed")
# def db_seed():
#     usa = Country(country_name="USA", country_capital="Washington", area=370000012)
#     germany = Country(country_name="Germany", country_capital="Berlin", area=83000000)
#     test_user = User(first_name="Success", last_name="Raphael", email="successraphael28@gmail.com", password="1234567890")
#
#     db.session.add(usa)
#     db.session.add(germany)
#     db.session.add(test_user)
#
#     db.session.commit()
#     print("Database seeded")
#
#
# @app.route("/")
# def homepage():
#     return jsonify({"message": "Fashion Business Management System API"})
#
# @app.route("/country/<int:country_id>", methods=['GET'])
# def get_country_by_id(country_id: int):
#     country = Country.query.get(country_id)
#
#     if not country:
#         return jsonify({"error":f"country with id {country_id} not found"}), 404
#
#     return jsonify(country_schema.dump(country))
#
# @app.route("/user/<int:user_id>", methods=['GET'])
# def get_user_by_id(user_id: int):
#     user = User.query.get(user_id)
#
#     if not user:
#         return jsonify({"error":"user not found"}), 404
#
#     return jsonify(user_schema.dump(user))
#
# @app.route("/add_country", methods=['POST'])
# def add_country():
#     country_name = request.form['country_name']
#     check_country = Country.query.filter_by(country_name=country_name).first()
#     if check_country:
#         return jsonify({"error":"Country already exists"})
#
#     capital = request.form["country_capital"]
#     area = request.form["area"]
#
#     new_country = Country(country_name=country_name, country_capital=capital, area=float(area))
#     db.session.add(new_country)
#     db.session.commit()
#
#     return jsonify({"success":f"{country_name} successfully added to the DB"}), 201
#
# @app.route("/add_user", methods=['POST'])
# def add_user():
#     user_email = request.form['email']
#     check_email = User.query.filter_by(email=user_email).first()
#     if check_email:
#         return jsonify({"error":"email already exists"}), 409
#
#     first_name = request.form.get("first_name")
#     last_name = request.form.get("last_name")
#     password = request.form.get("password")
#
#     new_user = User(first_name=str(first_name), last_name=str(last_name), email=user_email, password=str(password))
#
#     db.session.add(new_user)
#     db.session.commit()
#
#     return jsonify({"success":"user created successfully"}), 201
#
#
# @app.route("/add_another_country", methods=['POST'])
# def add_another_method_using_json():
#     data = request.get_json()
#     if not data:
#         return jsonify({"error":"Invalid or missing json data"}), 400
#
#     country_name = data.get("country_name")
#     check_country = Country.query.filter_by(country_name=country_name).first()
#     if check_country:
#         return jsonify("Country already exists"), 409
#
#     capital = data.get("country_capital")
#     area = data.get("area")
#     new_country = Country(country_name=country_name, country_capital=capital, area=area)
#
#     db.session.add(new_country)
#     db.session.commit()
#
#     return jsonify({"success":"New country added successfully"}), 201
#
#
# @app.route("/update_country/<int:country_id>", methods=['PATCH'])
# def update_country(country_id: int):
#     data = request.get_json()
#     if not data:
#         return jsonify({"error":"Invalid or missing json data"}), 404
#
#     country = Country.query.get(country_id)
#     if not country:
#         return jsonify({"error":"country not found"}), 404
#
#     if "country_name" in data:
#         country.country_name = data["country_name"]
#     if "country_capital" in data:
#         country.country_capital = data["country_capital"]
#     if "area" in data:
#         country.area = float(data["area"])
#
#     db.session.commit()
#     return jsonify({"success":"country updated successfully"}), 200
#
# # @app.route("/countries/<int:country_id>", methods=['DELETE'])
# @app.delete("/countries/<int:country_id>")
# def delete_country(country_id: int):
#     country = Country.query.filter_by(country_id=country_id).first()
#     if not country:
#         return jsonify({"error":"country not found"}), 409
#
#     db.session.delete(country)
#     db.session.commit()
#
#     return jsonify({"message":f"country with id {country_id} deleted"}), 202
#
# @app.route("/countries", methods=['GET'])
# def countries():
#     country_list = Country.query.all()
#     result = countries_schema.dump(country_list)
#     return jsonify(result)
#
# @app.route("/users", methods=['GET'])
# def users_():
#     users = User.query.all()
#     return jsonify(users_schema.dump(users))
#
#
# if __name__ == "__main__":
#     app.run()
