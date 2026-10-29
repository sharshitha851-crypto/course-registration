from app import app, registrations


def test_registered_courses():
    assert len(registrations) == 3
    assert registrations[0]["student"] == "Harshitha"
    assert registrations[0]["course_code"] == "CS101"
    assert registrations[1]["student"] == "Sathvika"
    assert registrations[2]["student"] == "Meenakshi"


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Course Registration System" in response.data
    assert b"Registered Courses" in response.data
    assert b"Harshitha" in response.data
    assert b"CS101" in response.data