class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    def calculate_salary(self):
        return self.salary * 12

employee1 = Employee("John", 1000)
employee1.show_details()
print(f"Annual Salary: {employee1.calculate_salary()}")