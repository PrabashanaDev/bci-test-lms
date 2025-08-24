from employee import BciAcademicEmployee, BciNonAcademicEmployee

employee1 = BciAcademicEmployee("001", "Malindu", 1000)
employee2 = BciNonAcademicEmployee("002", "Hirusha", 800)
employee3 = BciAcademicEmployee("003", "Udesh", 900)

employees = [employee1, employee2, employee3]

for employee in employees:
    if isinstance(employee, BciAcademicEmployee):
        employee.showBciAcademic()
    else:
        employee.showBciNonAcademic()

    print("Salary per Day:", employee.calculateSalary())
    print("Salary per Month:", employee.calculateSalary()*30)
    print("---------------------------------------------------")

