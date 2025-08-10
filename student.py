class Student:
    def __init__(self):
        self.stuID = ""
        self.stuName = ""
        self.stuAge = ""

    def setStudent(self, id, name, age):
        self.stuID = id
        self.stuName = name
        self.stuAge = age

    def showStudent(self):
        print(f"Student ID: {self.stuID}, Name: {self.stuName}, Age: {self.stuAge}")

student1 = Student()
student1.setStudent("001", "Chathura", "23")
student2 = Student()
student2.setStudent("002", "Akash", "22")
student3 = Student()
student3.setStudent("003", "Samidu", "21")

student1.showStudent()
student2.showStudent()
student3.showStudent()