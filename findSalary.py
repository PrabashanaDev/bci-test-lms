from employee import Academic, NonAcademic

employee1 = Academic("001", "Chathura", 1000, 8)
employee2 = NonAcademic("002", "Akash", 800, 8)
employee3 = Academic("003", "Samidu", 900, 8)






print("Academic Salary:", employee1.calculateSalary())
print("Non Academic Salary:", employee2.calculateSalary())
print("Academic Salary:", employee3.calculateSalary())

