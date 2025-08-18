from employee import Academic, NonAcademic

employee1 = Academic("001", "Chathura", 1000, 8)
employee2 = NonAcademic("002", "Akash", 800, 8)
employee3 = Academic("003", "Samidu", 900, 8)

employees = [employee1, employee2, employee3]

for employee in employees:
    if isinstance(employee, Academic):
        employee.showAcademic()
    else:
        employee.showNonAcademic()

    print("Salary:", employee.calculateSalary())


