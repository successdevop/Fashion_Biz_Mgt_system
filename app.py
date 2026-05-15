from flask import Flask, jsonify
from requests import request
from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route("/")
def homepage():
    return "Welcome to Success first flask project"

@app.route("/country/<int:country_id>", methods=['GET'])
def get_country_by_id(country_id: int):
    country = Country.query.get(country_id)

    if not country:
        return jsonify({"error":f"country with id {country_id} not found"}), 404

    return jsonify(country_schema.dump(country))

@app.route("/user/<int:user_id>", methods=['GET'])
def get_user_by_id(user_id: int):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error":"user not found"}), 404

    return jsonify(user_schema.dump(user))

@app.route("/add_country", methods=['POST'])
def add_country():
    country_name = request.form['country_name']
    check_country = Country.query.filter_by(country_name=country_name).first()
    if check_country:
        return jsonify({"error":"Country already exists"})

    country_capital = request.form['country_capital']
    area = request.form['area']
    

@app.route("/countries", methods=['GET'])
def countries():
    country_list = Country.query.all()
    result = countries_schema.dump(country_list)
    return jsonify(result)

@app.route("/users", methods=['GET'])
def users_():
    users = User.query.all()
    return jsonify(users_schema.dump(users))


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Country(db.Model):
    __tablename__ = "countries"
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String)
    country_capital = Column(String)
    area = Column(Float)


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "password")


class CountrySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Country
        fields = ("country_id", "country_name", "country_capital", "area")


user_schema = UserSchema()
users_schema = UserSchema(many=True)

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)


@app.cli.command("db_create")
def db_create():
    db.create_all()
    print("Database created")


@app.cli.command("db_drop")
def db_drop():
    db.drop_all()
    print("Database dropped")


@app.cli.command("db_seed")
def db_seed():
    usa = Country(country_name="USA", country_capital="Washington", area=370000012)
    germany = Country(country_name="Germany", country_capital="Berlin", area=83000000)
    test_user = User(first_name="Success", last_name="Raphael", email="successraphael28@gmail.com", password="1234567890")

    db.session.add(usa)
    db.session.add(germany)
    db.session.add(test_user)

    db.session.commit()
    print("Database seeded")


if __name__ == "__main__":
    app.run()
