from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    courses = ["Python", "Mad 1", "Mad 2"]
    student = {"Ram":"Mad 1", "Karan" : "Mad 2", "Saloni": "Python"}
    return render_template("index.html", html_courses = courses, html_student = student)

if __name__ == "__main__":
    app.run(debug = True)