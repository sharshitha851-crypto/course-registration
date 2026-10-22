courses = []


def add_course(course_name):
    courses.append(course_name)


def get_courses():
    return courses


if __name__ == "__main__":
    add_course("Python Programming")
    add_course("Database Management Systems")
    add_course("Computer Networks")

    print("Course List:")
    for course in get_courses():
        print(course)