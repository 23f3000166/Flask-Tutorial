# request is required when we're dealing with query parameters

from flask import Flask, request 


app = Flask(__name__)

# Single Query Parameter
@app.route("/search")
def search():
    name = request.args.get("name", "Guest")   
    
    # Guest is the default value if no name is present in the URL
    
    return f"Hello {name}"

# Multiple Query Parameter
@app.route("/student")
def student():
    name = request.args.get("name", "Guest")
    course = request.args.get("course", "Unknown")
    return f"{name} is learning {course}"

if __name__ == "__main__":
    app.run(debug = True)