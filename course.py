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
        
course1 = BciDegree("BSIT 1", "Information Technology")
course1.showCourse()


