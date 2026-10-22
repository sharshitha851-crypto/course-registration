from app import add_course, get_courses


def test_add_course():
    add_course("Software Engineering")
    assert "Software Engineering" in get_courses()