from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API"

# Static Routing
@app.route("/user")
def users():
    return "Welcome to User Page"

#Dynamic Routing
@app.route("/user/<name>")
def user(name):
    return "Hello " + name

#Dynamic routing with multiple routing parameters
@app.route("/student/<name>/<course>")
def student(name, course):
    return name + " is learning " + course



if __name__ == "__main__":
    app.run(debug = True)