from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self):
        self.empID = ""
        self.empName = ""

    def setEmployee(self, empID, empName):
        self.empID = empID
        self.empName = empName

    @abstractmethod
    def calculateSalary(self):
        pass

class Academic(Employee):
    def __init__(self):
        self.hourRate = ""
        self.hourWork = ""

    def setAcademic(self, hourRate, hourWork):
        self.hourRate = hourRate
        self.hourWork = hourWork

    def calculateSalary(self):
        return self.hourRate * self.hourWork


class NonAcademic(Employee):
    def __init__(self):
        self.NhourRate = ""
        self.hourWork = ""    
    
    def setNonAcademic(self, hourRate, hourWork):
        self.hourRate = hourRate
        self.hourWork = hourWork

    def calculateSalary(self):
        return self.NhourRate * self.hourWork


