# A class should have one, and only one, reason to change, meaning it should have only one job or responsibility.

# Bad example
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_payroll(self):
        return self.salary

    def generate_report(self):
        return f"Employee Report for {self.name}"

# Good example (Separate responsibilities into different classes)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Payroll:
    def calculate_payroll(self, employee):
        return employee.salary

class Report:
    def generate_report(self, employee):
        return f"Employee Report for {employee.name}"
