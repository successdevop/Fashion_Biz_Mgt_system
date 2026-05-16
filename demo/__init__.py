from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from demo.models.country import CountryModel
from demo.models.user import UserSchema


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fashion_biz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route("/")
def home():
    return jsonify({"message": "Welcome To Fashion Business Management System API"})


@app.cli.command("create_db")
def create_db():
    db.create_all()
    print("DATABASE created")


@app.cli.command("drop_db")
def drop_db():
    db.drop_all()
    print("DATABASE dropped")


@app.cli.command("db_seed")
def db_seed():
    usa = CountryModel(country_name="Nigeria", country_capital="Abuja", country_population=200000349)
    user = UserSchema(first_name="Success", last_name="Raphael", email="successraphael28@gmail.com",
                      password="password")

    db.session.add(usa)
    db.session.add(user)
    db.session.commit()

    print("DATABASE seeded")

