class Employee:
    def __init__(self):
        self.empID = ""
        self.empName = ""

    def setEmployee(self, empID, empName):
        self.empID = empID
        self.empName = empName

    def showEmployee(self):
        print(f"Employee Id: {self.empID} Employee Name: {self.empName}")

class Academic(Employee):
    def __init__(self):
        self.hourRate = ""
        self.hourWork = ""

    def setAcademic(self, hourRate, hourWork):
        self.hourRate = hourRate
        self.hourWork = hourWork

    def showAcademic(self):
        print(f"Salary is: {self.hourRate*self.hourWork} for a day")

class NonAcademic(Employee):
    def __init__(self):
        self.NhourRate = ""
        self.hourWork = ""
    
    def setNonAcademic(self, hourRate, hourWork):
        self.hourRate = hourRate
        self.hourWork = hourWork

    def showNonAcademic(self):
        print(f"Salary is: {self.hourRate*self.hourWork} for a day")


