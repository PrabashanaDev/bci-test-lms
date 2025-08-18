from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, empID, empName):
        self.empID = empID
        self.empName = empName

    def showEmployee(self):
        print(f"Employee ID: {self.empId}, Employee name: {self.empName}")

    @abstractmethod
    def calculateSalary(self):
        pass

class Academic(Employee):
    def __init__(self, empID, empName, hourRate, hourWork):
        super().__init__(empID, empName)
        self.hourRate = hourRate
        self.hourWork = hourWork
    
    def showAcademic(self):
        print(f"Academic Employee Name: {self.empName}, Employee ID: {self.empID}, Hour Rate: {self.hourRate}, Work hours: {self.hourWork}")

    def calculateSalary(self):
        return self.hourRate * self.hourWork


class NonAcademic(Employee):
    def __init__(self, empID, empName, hourRate, hourWork):
        super().__init__(empID, empName)
        self.hourRate = hourRate
        self.hourWork = hourWork    

    def showNonAcademic(self):
        print(f"Non Academic Employee Name: {self.empName}, Employee ID: {self.empID},Hour Rate: {self.hourRate}, Work hours: {self.hourWork}")

    def calculateSalary(self):
        return self.hourRate * self.hourWork
    
if __name__ == "__main__":
    
    employee1 = Academic("001", "Chathura", 1000, 8)
    employee2 = NonAcademic("002", "Akash", 800, 8)
    employee3 = Academic("003", "Samidu", 900, 8)

    employee1.showAcademic()
    employee2.showNonAcademic()
    employee3.showAcademic()
