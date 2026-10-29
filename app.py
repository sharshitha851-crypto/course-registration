from flask import Flask, render_template

app = Flask(__name__)

registrations = [
    {"student": "Harshitha", "course_code": "CS101", "course_name": "Python Programming"},
    {"student": "Sathvika", "course_code": "CS102", "course_name": "Database Management Systems"},
    {"student": "Meenakshi", "course_code": "CS103", "course_name": "Computer Networks"}
]


@app.route("/")
def home():
    return render_template("index.html", registrations=registrations)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)