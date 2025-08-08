class student:
    def __init__(self):
        self.stuID = ""
        self.stuName = ""
        self.stuAge = ""

    def setstudent(self, id, name, age):
        self.stuID = id
        self.stuName = name
        self.stuAge = age

    def showstudent(self):
        print(f"Student ID: {self.stuID}, Name: {self.stuName}, Age: {self.stuAge}")

student1 = student()
student1.setstudent("001", "Chathura", "23")
student2 = student()
student2.setstudent("002", "Akash", "22")
student3 = student()
student3.setstudent("003", "Samidu", "21")

student1.showstudent()
student2.showstudent()
student3.showstudent()