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

    def calAvg(self, marks):
        return marks

class BciDiploma(Course):
    def __init__(self, courID, courName):
        super().__init__()
        self.setCourse(courID, courName)

    def showCourse(self):
        print(f"Course ID: {self.courID}, Course Name: {self.courName}")

    def calAvg(self, marks):
        return marks

class BciCertificate(Course):
    def __init__(self, courID, courName):
        super().__init__()
        self.setCourse(courID, courName)

    def showCourse(self):
        print(f"Course ID: {self.courID}, Course Name: {self.courName}")

    def calAvg(self, marks):
        return marks

if __name__ == "__main__":

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
