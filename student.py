from abc import ABC, abstractmethod
class Student(ABC):
    TotalStudents = 0
    result = 0
    def __init__(self):
        self.stuID = ""
        self.stuName = ""
        self.stuAge = ""
        self.stuCourse = ""
        self.stuFinalResult = ""
        self.stuAddress = ""
        Student.TotalStudents += 1

    def setStudent(self, stuID, stuName, stuAge, stuCourse, stuFinalResult, stuAddress):
        self.stuID = stuID
        self.stuName = stuName
        self.stuAge = stuAge
        self.stuCourse = stuCourse
        self.stuFinalResult = stuFinalResult
        self.stuAddress = stuAddress

    

    def showStudent(self):
        print(f"Student ID: {self.stuID}, Name: {self.stuName}, Age: {self.stuAge}")

    def setCourse(self, course):
        self.course = course

    def stuMarks(self, marks):
        self.marks = marks

    @abstractmethod
    def showStudent(self):
        pass
    def avg(self):
        pass

class BciPostGraduate(Student):
    def showStudent(self):
        print(" \nStudent ID: {} \nStudent Name: {} \nStudent Course: {} \nStudent Age: {} \nStudent Final Result: {} \nStudent Address: {}".format(self.stuID, self.stuName, self.stuCourse, self.stuAge, self.stuFinalResult, self.stuAddress))

    def avg():
        print("Total Avg: ", Student.result/Student.TotalStudents)  

class BciUnderGraduate(Student):
    def showStudent(self):
        print(" \nStudent ID: {} \nStudent Name: {} \nStudent Course: {} \nStudent Age: {} \nStudent Final Result: {} \nStudent Address: {}".format(self.stuID, self.stuName, self.stuCourse, self.stuAge, self.stuFinalResult, self.stuAddress))

    def avg():
        print("Total Avg: ", Student.result/Student.TotalStudents)

Student1 = BciPostGraduate()
Student1.setStudent("001", "Chathura", "BSIT", "24", "90", "ABC ROAD")

Student1.showStudent()



    



