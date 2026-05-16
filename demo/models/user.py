from sqlalchemy import Column, Integer, String
from demo import db


class UserSchema(db.Model):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


    def __repr__(self):
        return f"User(user_id:{self.user_id} | first_name:{self.first_name} | email:{self.email})"