from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self):
        self.courID = ""
        self.courName = ""
    
    def setCourse(self, courID, courName):
        self.courID = courID
        self.courName = courName

    @abstractmethod
    def calAvg(self):
        pass


class BciDegree(Course):
    def __init__(self, courID, courName):
        super().__init__()
        self.setCourse(courID, courName)

    def showCourse(self):
        print(f"Course ID: {self.courID}, Course Name: {self.courName}")

    def calAvg(self):
        pass

class BciDiploma(Course):
    def __init__(self, courID, courName):
        super().__init__()
        self.setCourse(courID, courName)

    def showCourse(self):
        print(f"Course ID: {self.courID}, Course Name: {self.courName}")

    def calAvg(self):
        pass

class BciCertificate(Course):
    def __init__(self, courID, courName):
        super().__init__()
        self.setCourse(courID, courName)

    def showCourse(self):
        print(f"Course ID: {self.courID}, Course Name: {self.courName}")

    def calAvg(self):
        pass

if __name__ == "__main__":

    course1 = BciDegree("BSIT 1", "Information Technology")
    course1.showCourse()

    course2 = BciDiploma("AE 1", "Aquinas English")
    course2.showCourse()

    course3 = BciCertificate("R 1", "Robotics")
    course3.showCourse()
