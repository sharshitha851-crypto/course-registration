from app import app, courses, registrations


def test_courses():
    assert len(courses) == 4
    assert courses[0]["code"] == "CS101"
    assert courses[0]["name"] == "Python Programming"


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Course Registration System" in response.data
    assert b"Register for a Course" in response.data


def test_registration():
    client = app.test_client()

    response = client.post(
        "/register",
        data={
            "student_name": "Harshitha",
            "course_code": "CS101"
        }
    )

    assert response.status_code == 200
    assert b"Registration Successful" in response.data
    assert b"Harshitha" in response.data
    assert b"CS101" in response.data