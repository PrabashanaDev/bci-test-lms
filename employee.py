class Employee:
    def __init__(self):
        self.empID = ""
        self.empName = ""

    def setEmployee(self, empID, empName):
        self.empID = empID
        self.empName = empName

    def showEmployee(self):
        print(f"Employee Id: {self.empID} Employee Name: {self.empName}")

employee1 = Employee()
employee1.setEmployee("001", "Chathura")

employee1.showEmployee()