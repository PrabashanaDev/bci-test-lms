from student import Student

student1 = Student("001", "Chathura Prabashana", "24")
student2 = Student("002", "Akash Vishmitha", "23")
student3 = Student("003", "Samidu Kaushalya", "22")

students = [student1, student2, student3]

student1.stuMarks(90)
student2.stuMarks(100)
student3.stuMarks(95)

avg = (student1.marks + student2.marks + student3.marks)/len(students)

print(f"Average Marks: {avg}")