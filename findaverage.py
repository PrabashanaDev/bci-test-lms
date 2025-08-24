from student import BciPostGraduate, BciUnderGraduate

student1 = BciPostGraduate()
student1.setStudent("001", "Chathura", "14", "BSIT", "ABC ROAD")

student2 = BciPostGraduate()
student2.setStudent("002", "Akash", "23", "BSIT", "Colombo ROAD")

student3 = BciUnderGraduate()
student3.setStudent("003", "Samidu", "22", "BSSE", "Negombo ROAD")


students = [student1, student2, student3]

student1.stuMarks(90)
student2.stuMarks(100)
student3.stuMarks(80)

avg = sum([s.marks for s in students]) / len(students)
print(f"Average Marks: {avg}")
