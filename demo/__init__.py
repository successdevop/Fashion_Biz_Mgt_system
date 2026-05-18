from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fashion_biz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'successRaphaelIfeanyichukwu123@/.com'

db = SQLAlchemy(app)
ma = Marshmallow(app)
auth = HTTPBasicAuth()
jwt = JWTManager(app=app)

from demo.controllers import user_controller
from demo.auth import login, verify_password
from demo import commands
