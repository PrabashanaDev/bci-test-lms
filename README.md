# BCI LMS – (Pre-release v3.0.0-pre)

A simple Python OOP mini-system that demonstrates **Encapsulation, Inheritance, Abstraction, and Composition** across Students, Courses, Employees, Faculties, and Campus.

## Structure
- `student.py` – Student entity (private attributes, course assignment, marks, average)
- `course.py` – Abstract `Course` + concrete `Degree`, `Diploma`, `Certificate` (different average logic)
- `employee.py` – Abstract `Employee` + `Academic` (hourly) and `NonAcademic` (base + commission)
- `faculty.py` – Holds students, courses, employees
- `campus.py` – Holds faculties
- `findaverage.py` – Creates campus/faculty/courses/students and prints averages
- `findSalary.py` – Creates campus/faculty/employees and prints salaries

## Run
```bash
python findaverage.py
python findSalary.py


