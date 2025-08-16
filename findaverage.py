from student import Student
from course import Degree, diploma, certificate

student1 = Student("001", "Chathura", "23")
student2 = Student("002", "Akash", "22")
student3 = Student("003", "Samidu", "21")

student1.setCourse(Degree("BSIT"))
student2.setCourse(certificate("BSSE"))
student3.setCourse(diploma("Aquinas"))