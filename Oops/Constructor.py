
class student:
    def __init__(self, name, age, course, Salary):
        self.name = name
        self.age = age
        self.course = course
        self.Salary = Salary

    def display_info(self):
        print(f"{self.name}, {self.age}, {self.course}")

    def tax(self):
        if self.Salary >= 50000:
            return self.Salary * 0.10
        return 0

student1 = student("Ram", 30, "QA", 50000)
student2 = student("Krish", 20, "UKG", 40000)
student3 = student("Sasu", 28, "12th", 60000)


student1.display_info()
student2.display_info()

print(student2.tax())
print(student1.tax())
print(student3.tax())