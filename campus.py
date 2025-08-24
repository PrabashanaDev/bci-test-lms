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
print("Home")
print("------------------------------------------------------")
print("             Welcome to BCI Campus")

print("------------------------------------------------------")
print("About")
print("------------------------------------------------------")

print("------------------------------------------------------")
print("Courses")
print("------------------------------------------------------")

class courses(Campus):
    course1 = BciDegree("001", "(BSIT) Information Technology")
    course1.showCourse()

    course2 = BciDegree("002", "(BSSE) Software Engineering")
    course2.showCourse()

    course3 = BciDegree("003", "(BMS) Business Management")
    course3.showCourse()

    course4 = BciDiploma("004", "Aquinas English")
    course4.showCourse()

    course5 = BciCertificate("005", "Robotics")
    course5.showCourse()

print("------------------------------------------------------")
print("Faculties")
print("------------------------------------------------------")

class faculties(Campus):
    Faculty1 = BCIFaculty("School of Computing", "Dr.Waruna Premachandra", "001")
    Faculty2 = BCIFaculty("School of Business", "Dr.Tharanga Rathnayaka", "002")
    Faculty3 = BCIFaculty("School of Education", "Rev.Dr.George Perera", "003")
    

    Faculty1.show_facultyNames()
    Faculty2.show_facultyNames()
    Faculty3.show_facultyNames()
