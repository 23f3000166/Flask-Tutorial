from flask import Flask
from uuid import UUID

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API"

#URL convertor - Integer Convertor
@app.route("/user/<int:id>")
def user(id):
    return f"User id {id}"

#URL convertor - Float Convertor
@app.route("/price/<float:price>")
def price(price):
    return f"Price is {price}"

#URL convertor - String Convertor
@app.route("/users/<string:name>")
def users(name):
    return f"Hello {name}"

#URL convertor - Path Convertor
@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

#URL convertor - UUID Convertor
@app.route("/student/<uuid:student_id>")
def student(student_id):
    return str(student_id)

if __name__ == "__main__":
    app.run(debug = True)