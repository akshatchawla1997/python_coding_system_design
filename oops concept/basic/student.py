class Student:
    name = "John"
    marks = 90

    def show_details(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
    
    def calculate_percentage(self):
        return (self.marks / 100) * 100

student1 = Student()
student1.show_details()
print(student1.calculate_percentage())