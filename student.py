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

    

    

    def setCourse(self, course):
        self.course = course

    @abstractmethod
    def showStudent(self):
        pass

    def stuMarks(self, marks):
        self.marks = marks

    @abstractmethod
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

if __name__ == "__main__":

    student1 = BciPostGraduate()
    student1.setStudent("001", "Chathura", "14", "BSIT", "90", "ABC ROAD")
    student1.showStudent()

    student2 = BciPostGraduate()
    student2.setStudent("002", "Akash", "23", "BSIT", "80", "Colombo ROAD")
    student2.showStudent()

    student3 = BciUnderGraduate()
    student3.setStudent("003", "Samidu", "22", "BSSE", "70", "Negombo ROAD")
    student3.showStudent()





    



