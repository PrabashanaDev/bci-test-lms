from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, empID, empName, empSalary):
        self.empID = empID
        self.empName = empName
        self.empSalary = empSalary

    @abstractmethod
    def calculateSalary(self):
        pass

class BciAcademicEmployee(Employee):
    def __init__(self, empID, empName, empSalary):
        super().__init__(empID, empName, empSalary)
    
    def showBciAcademic(self):
        print(f"Academic Employee ID: {self.empID}, Academic Employee Name: {self.empName}, Salary: {self.empSalary}")
    
    def calculateSalary(self):
        return round(self.empSalary * 1.3)


class BciNonAcademicEmployee(Employee):
    def __init__(self, empID, empName, empSalary):
        super().__init__(empID, empName, empSalary)  

    def showBciNonAcademic(self):
        print(f"Non Academic Employee ID: {self.empID}, Non Academic Employee Name: {self.empName}, Basic Salary: {self.empSalary}")

    def calculateSalary(self):
        return round(self.empSalary * 1.1)
    
if __name__ == "__main__":

    employee1 = BciAcademicEmployee("001", "Malindu", 1000)
    employee2 = BciNonAcademicEmployee("002", "Hirusha", 800)
    employee3 = BciAcademicEmployee("003", "Udesh", 900)
    
    employee1.showBciAcademic()
    employee2.showBciNonAcademic()
    employee3.showBciAcademic()
