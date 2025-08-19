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

    student1 = Student("001", "Chathura Prabashana", "24")
    student2 = Student("002", "Akash Vishmitha", "23")
    student3 = Student("003", "Samidu Kaushalya", "22")

    student1.setCourse(Degree("BSIT (Information Technology)"))
    student2.setCourse(certificate("Robotic Certificate"))
    student3.setCourse(diploma("Aquinas English Diploma"))

    

    students = [student1, student2, student3]


    for student in students:
        student.showStudent()
        if isinstance(student.course, Degree):
            print("Course Type: Degree")
        elif isinstance(student.course, diploma):
            print("Course Type: Diploma")
        else:
            print("Course Type: Certificate")

    



