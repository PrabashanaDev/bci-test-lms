from student import BciPostGraduate, BciUnderGraduate

student1 = BciPostGraduate()
student1.setStudent("001", "Chathura", "14", "BSIT", "90", "ABC ROAD")
student1.showStudent()

student2 = BciPostGraduate()
student2.setStudent("002", "Akash", "23", "BSIT", "80", "Colombo ROAD")
student2.showStudent()

student3 = BciUnderGraduate()
student3.setStudent("003", "Samidu", "22", "BSSE", "70", "Negombo ROAD")
student3.showStudent()

students = [student1, student2, student3]

student1.stuMarks(90)
student2.stuMarks(100)
student3.stuMarks(80)

avg = sum([s.marks for s in students]) / len(students)
print(f"Average Marks: {avg}")
