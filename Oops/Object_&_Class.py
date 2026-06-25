#Class and Object Example:

class Car:
    def __init__(self, brand, color):
        self.brand = brand   # attribute
        self.color = color   # attribute

    def drive(self):         # method
        print(f"The {self.color} {self.brand} is driving.")

# Creating objects from the Car class
car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

car1.drive()   # Output: The Red Toyota is driving.
car2.drive()   # Output: The Black BMW is driving.
