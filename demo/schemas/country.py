from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from demo.models.country import CountryModel


class CountrySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CountryModel
        fields = ("country_id", "country_name", "country_capital", "country_population")

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)