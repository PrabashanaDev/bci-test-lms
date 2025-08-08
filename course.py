class Course:
    def __init__(self):
        self.course_id = ""
        self.course_name = ""

    def setCourse(self, courID, courName):
        self.courID = courID
        self.courName = courName

    def showCourse(self):
        print(f"Course ID: {self.courID}, Course Name: {self.courName}")


    

course1 = Course()
course1.setCourse("001", "Software Engineering")
course2 = Course()
course2.setCourse("002", "Information Technology")

course1.showCourse()
course2.showCourse()
