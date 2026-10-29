from flask import Flask, render_template, request

app = Flask(__name__)

courses = [
    {"code": "CS101", "name": "Python Programming"},
    {"code": "CS102", "name": "Database Management Systems"},
    {"code": "CS103", "name": "Computer Networks"},
    {"code": "CS104", "name": "Artificial Intelligence"}
]

registrations = []


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", courses=courses)


@app.route("/register", methods=["POST"])
def register():
    student_name = request.form["student_name"]
    course_code = request.form["course_code"]

    registrations.append({
        "student": student_name,
        "course": course_code
    })

    return render_template(
        "success.html",
        student_name=student_name,
        course_code=course_code
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)