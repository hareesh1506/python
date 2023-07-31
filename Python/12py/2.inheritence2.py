from abc import ABC, abstractmethod

# Base class: Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Salary: ${self.salary}"

# Abstract class: Department
class Department(ABC):
    @abstractmethod
    def get_department_name(self):
        pass

# Derived class: Faculty
class Faculty(Employee, Department):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

    def display_info(self):
        return f"{super().display_info()}, Department: {self.department}"

    def get_department_name(self):
        return self.department

# Derived class: Staff
class Staff(Employee, Department):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

    def display_info(self):
        return f"{super().display_info()}, Department: {self.department}"

    def get_department_name(self):
        return self.department

# Derived class: Researcher
class Researcher(Employee, Department):
    def __init__(self, name, salary, department, research_area):
        Employee.__init__(self, name, salary)
        self.department = department
        self.research_area = research_area

    def display_info(self):
        return f"{super().display_info()}, Department: {self.department}, Research Area: {self.research_area}"

    def get_department_name(self):
        return self.department

# Main function to demonstrate inheritance
def main():
    faculty1 = Faculty("John Doe", 60000, "Computer Science")
    staff1 = Staff("Jane Smith", 45000, "Administration")
    researcher1 = Researcher("Alice Johnson", 70000, "Biology", "Genetics")

    print(faculty1.display_info())
    print(f"Department Name: {faculty1.get_department_name()}")

    print(staff1.display_info())
    print(f"Department Name: {staff1.get_department_name()}")

    print(researcher1.display_info())
    print(f"Department Name: {researcher1.get_department_name()}")

if __name__ == "__main__":
    main()
