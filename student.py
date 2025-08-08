class student:
    def __init__(self, stuID, stuName, stuAge):
        self.stuID = stuID
        self.stuName = stuName
        self.stuAge = stuAge

student1 = student("001", "Chathura", "23")
student2 = student("002", "Akash", "22")
student3 = student("003", "Samidu", "21")

students = [student1, student2, student3]

for student in students:
    print(f"Student ID: {student.stuID} Name: {student.stuName}, Age: {student.stuAge}")


        