# from _testcapi import error
# from flask import Flask, jsonify, request
#
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "hello world", 200
#
# @app.route("/simple")
# def simple():
#     return jsonify(text="Simple is the new standard. So watch out",
#                    message="Testing my flask api")
#
# @app.route("/not_found")
# def not_found():
#     return jsonify(error="not found"), 404
#
#
# @app.route("/parameter")
# def parameter():
#     name = request.args.get("name")
#     age = int(request.args.get("age", 0))
#     if age > 18:
#         return f"Congratulations {name}, You are eligible"
#     else:
#         return f"sorry {name}, You are not eligible to access this API"
#
#
# @app.route("/api_variable/<string:name>/<int:age>")
# def api_variable(name: str, age: int):
#     if age > 18:
#         return f"Congratulations {name}, you are eligible"
#     else:
#         return f"Sorry {name}, you are not allowed to use this API at this age"
from operator import add

# if __name__ == "__main__":
#     app.run()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///test.db")
Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.commit()

query = session.get(Employee, 5)
session.delete(query)
session.commit()

# query = session.query(Employee).filter(Employee.id>1)
# for emp in query:
#     print(emp.name, emp.position)