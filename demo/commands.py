from demo import app
from demo.models.user import UserModel
from demo.models.country import CountryModel
from demo import db

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
    user = UserModel(first_name="Success", last_name="Raphael", email="successraphael28@gmail.com",
                     password="password")

    db.session.add(usa)
    db.session.add(user)
    db.session.commit()

    print("DATABASE seeded")