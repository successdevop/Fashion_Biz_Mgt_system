from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from demo.models.user import UserModel


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        fields = ("user_id", "first_name", "last_name", "email", "password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)