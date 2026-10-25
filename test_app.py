from app import app, courses


def test_courses():
    assert len(courses) == 4
    assert courses[0]["code"] == "CS101"
    assert courses[0]["name"] == "Python Programming"
    assert courses[1]["code"] == "CS102"
    assert courses[2]["code"] == "CS103"
    assert courses[3]["code"] == "CS104"


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Course Registration System" in response.data