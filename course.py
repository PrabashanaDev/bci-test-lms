class Course:
    def __init__(self):
        self.course_id = ""
        self.course_name = ""

    def setCourse(self, courID, courName):
        self.courID = courID
        self.courName = courName

    def showCourse(self):
        print(f"Course ID: {self.courID}, Course Name: {self.courName}")


class Degree(Course):
    def __init__(self):
        pass

class diploma(Course):
    def __init__(self):
        pass

class certificate():
    def __init__(self):
        pass
    

