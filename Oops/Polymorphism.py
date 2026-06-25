# 1. Method Overriding (Run-time Polymorphism)

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):  # overrides parent method
        print("Dog barks")

class Cat(Animal):
    def speak(self):  # overrides parent method
        print("Cat meows")

# Polymorphism in action
animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.speak()

# Method Overloading (Simulated in Python)
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5, 10))       # 2 arguments
print(calc.add(5, 10, 15))   # 3 arguments
print(calc.add(5))           # 1 argument

# 3. Polymorphism with Functions
def add(x, y):
    return x + y

print(add(5, 10))        # integers
print(add("Hello ", "World"))  # strings
print(add([1, 2], [3, 4]))     # lists
