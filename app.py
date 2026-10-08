from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    f_name = 'Rajat'
    l_name = "Sood"
    course = ["Mad 1", 'Mad 2', "DBMS"]
    roll = 20213
    price = 500
    return render_template("index.html",
                           html_fname = f_name,
                           html_lname = l_name,
                           html_course = course,
                           html_roll = roll,
                           html_price = price)

if __name__ == "__main__":
    app.run(debug = True)