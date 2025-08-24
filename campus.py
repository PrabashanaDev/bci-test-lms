from abc import ABC, abstractmethod
from faculty import Faculty
class Campus(ABC):
    def __init__(self, campusName, campusLocation):
        self.campusName = campusName
        self.campusLocation = campusLocation

    @abstractmethod
    def showCampusDetails(self):
        pass

class Faculty(Campus):
    Faculty1.show_facultyNames()
    Faculty2.show_facultyNames()
    Faculty3.show_facultyNames()
    Faculty4.show_facultyNames()
