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

