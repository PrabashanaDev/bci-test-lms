class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

course1 = Course("001", "Software Engineering")
course2 = Course("002", "Information Technology")

courses = [course1, course2]

for course in courses:
    print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")
