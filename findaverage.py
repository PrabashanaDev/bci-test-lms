from student import Student
from course import Degree, diploma, certificate

student1 = Student("001", "Chathura", "23")
student2 = Student("002", "Akash", "22")
student3 = Student("003", "Samidu", "21")



student1.stuMarks(90)
student2.stuMarks(100)
student3.stuMarks(95)

avg = (student1.marks + student2.marks + student3.marks) / 3
print(f"Average Marks: {avg}")