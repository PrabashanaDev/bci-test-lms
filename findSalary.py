from employee import Academic, NonAcademic

academic1 = Academic("001", "Chathura", 1000, 8)
academic1.showAcademic()
print("Academic Salary:", academic1.calculateSalary())

nonAcademic1 = NonAcademic("999", "Akash", 800, 8)
nonAcademic1.showNonAcademic()
print("Non Academic Salary:", nonAcademic1.calculateSalary())