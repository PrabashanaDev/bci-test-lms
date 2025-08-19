from abc import ABC, abstractmethod

class Faculty(ABC):
    def __init__(self, faculty_Name, faculty_Head, faculty_ID):
        self.faculty_Name = faculty_Name
        self.faculty_Head = faculty_Head
        self.faculty_ID = faculty_ID

    @abstractmethod
    def show_facultyNames(self):
        pass

class BCIFaculty(Faculty):
    def show_facultyNames(self):
        print(f"Faculty Name: {self.faculty_Name}, faculty Head: {self.faculty_Head}, faculty ID: {self.faculty_ID}")

Faculty1 = BCIFaculty("School of Computing", "Dr.Waruna", "001")
Faculty2 = BCIFaculty("School of Business", "Chathura", "002")
Faculty3 = BCIFaculty("School of Education", "Chathura", "003")
Faculty4 = BCIFaculty("School of English", "Chathura", "004")

Faculty1.show_facultyNames()
Faculty2.show_facultyNames()
Faculty3.show_facultyNames()
Faculty4.show_facultyNames()
        