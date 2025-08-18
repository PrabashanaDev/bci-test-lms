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

    student1.showStudent()
    student2.showStudent()
    student3.showStudent()

