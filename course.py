from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, courID, courName):
        self.courID = courID
        self.courName = courName


    def showCourse(self):
        print(f"Course ID: {self.courID}, Course Name: {self.courName}")

    def setCourse(self, courName):
        self.courName = courName

    @abstractmethod
    def calAvg(self):
        pass


class Degree(Course):
    subjects= 5
    def __init__(self, degName):
        self.degName = degName
    def showDegree(self):
        print(f"Degree Name: {self.degName}")
    def calAvg(self):
        pass

class diploma(Course):
    subjects = 3
    def __init__(self, dipName):
        self.dipName = dipName
    def showDiploma(self):
        print(f"Diploma Name: {self.dipName}")
    def calAvg(self):
        pass

class certificate(Course):
    subjects = 2
    def __init__(self, certName):
        self.certName = certName
    def showCertificate(self):
        print(f"Certificate Name: {self.certName}")
    def calAvg(self):
        pass

if __name__ == "__main__":

    degree1 = Degree("BSIT")
    degree2 = Degree("BSSE")

    diploma1 = diploma("Aquinas")

    certificate1 = certificate("Robotic")


    degree1.showDegree()
    degree2.showDegree()
    diploma1.showDiploma()
    certificate1.showCertificate()



