from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/simple")
def simple():
    return jsonify(text="Simple is the new standard. So watch out",
                   message="Testing my flask api")

if __name__ == "__main__":
    app.run()

