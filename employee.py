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
    
    def show_employee(self):
        print(f"Academic Employee ID: {self.empID}, Academic Employee Name: {self.empName}, Salary: {self.empSalary}")
    
    def calculateSalary(self):
        pass


class BciNonAcademicEmployee(Employee):
    def __init__(self, empID, empName, empSalary):
        super().__init__(empID, empName, empSalary)  

    def show_employee(self):
        print(f"Non Academic Employee ID: {self.empID}, Non Academic Employee Name: {self.empName}, Salary: {self.empSalary}")

    def calculateSalary(self):
        pass
    
Employee1 = BciAcademicEmployee("001","Chathura","50000")
Employee1.show_employee()
