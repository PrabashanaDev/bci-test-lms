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

if __name__ == "__main__":

    Faculty1 = BCIFaculty("School of Computing", "Dr.Waruna Premachandra", "001")
    Faculty2 = BCIFaculty("School of Business", "Dr.Tharanga Rathnayaka", "002")
    Faculty3 = BCIFaculty("School of Education", "Rev.Dr.George Perera", "003")
    

    Faculty1.show_facultyNames()
    Faculty2.show_facultyNames()
    Faculty3.show_facultyNames()
    
        