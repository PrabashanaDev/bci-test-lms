from course import Degree, diploma, certificate
class Student:
    def __init__(self, id, name, age):
        self.stuID = id
        self.stuName = name
        self.stuAge = age

    

    def showStudent(self):
        print(f"Student ID: {self.stuID}, Name: {self.stuName}, Age: {self.stuAge}")

    def setCourse(self, course):
        self.course = course

    def stuMarks(self, marks):
        self.marks = marks
        

if __name__ == "__main__":

    student1 = Student("001", "Chathura", "23")
    student2 = Student("002", "Akash", "22")
    student3 = Student("003", "Samidu", "21")

    student1.setCourse(Degree("BSIT"))
    student2.setCourse(certificate("BSSE"))
    student3.setCourse(diploma("Aquinas"))

    

students = [student1, student2, student3]


for student in students:
    student.showStudent()
    if isinstance(student.course, Degree):
        print("Course Type: Degree")
    elif isinstance(student.course, diploma):
        print("Course Type: Diploma")
    else:
        print("Course Type: Certificate")

    



