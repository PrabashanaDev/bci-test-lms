from student import BciPostGraduate

student1 = BciPostGraduate()
student1.setStudent("001", "Chathura", 14, "BSIT", 90, "ABC ROAD")

student2 = BciPostGraduate()
student2.setStudent("002", "Akash Vishmitha", 23, "AE", 100, "DEF ROAD")

student3 = BciPostGraduate()
student3.setStudent("003", "Samidu Kaushalya", 22, "R", 95, "GHI ROAD")

students = [student1, student2, student3]

student1.stuMarks(90)
student2.stuMarks(100)
student3.stuMarks(95)

avg = sum([s.marks for s in students]) / len(students)
print(f"Average Marks: {avg}")
