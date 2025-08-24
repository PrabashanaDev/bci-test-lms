from abc import ABC, abstractmethod
from course import BciDegree,BciDiploma,BciCertificate
from faculty import BCIFaculty
class Campus(ABC):
    def __init__(self, campusName, campusLocation):
        self.campusName = campusName
        self.campusLocation = campusLocation

    @abstractmethod
    def showCampusDetails(self):
        pass

print("------------------------------------------------------")
print("Courses")
print("------------------------------------------------------")

class courses(Campus):
    course1 = BciDegree("BSIT 1", "Information Technology")
    course1.showCourse()

    course2 = BciDiploma("AE 1", "Aquinas English")
    course2.showCourse()

    course3 = BciCertificate("R 1", "Robotics")
    course3.showCourse()

print("------------------------------------------------------")
print("Faculties")
print("------------------------------------------------------")

class faculties(Campus):
    Faculty1 = BCIFaculty("School of Computing", "Dr.Waruna", "001")
    Faculty2 = BCIFaculty("School of Business", "Chathura", "002")
    Faculty3 = BCIFaculty("School of Education", "Chathura", "003")
    Faculty4 = BCIFaculty("School of English", "Chathura", "004")

    Faculty1.show_facultyNames()
    Faculty2.show_facultyNames()
    Faculty3.show_facultyNames()
    Faculty4.show_facultyNames()
