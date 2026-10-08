from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    name = 'Rajat'
    course = "Mad 1"
    roll = 20213
    return render_template("index.html",
                           html_name = name,
                           html_course = course,
                           html_roll = roll)

if __name__ == "__main__":
    app.run(debug = True)