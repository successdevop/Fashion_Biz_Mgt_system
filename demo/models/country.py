from sqlalchemy import Column, Integer, String, Float
from demo.repository.repo import db


class CountryModel(db.Model):
    __tablename__ = "countries"
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String, nullable=False)
    country_capital = Column(String, nullable=False)
    country_population = Column(Float, nullable=False)


    def __repr__(self):
        return f"Country(country_id:{self.country_id} | country_name:{self.country_name})"