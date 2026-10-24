from flask import Flask, render_template

app = Flask(__name__)

courses = [
    {"code": "CS101", "name": "Python Programming"},
    {"code": "CS102", "name": "Database Management Systems"},
    {"code": "CS103", "name": "Computer Networks"},
    {"code": "CS104", "name": "Artificial Intelligence"}
]

@app.route("/")
def home():
    return render_template("index.html", courses=courses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)