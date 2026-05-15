from flask import Flask
from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
db = SQLAlchemy(app)


@app.route("/")
def homepage():
    return "Welcome to Success first flask project"


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
