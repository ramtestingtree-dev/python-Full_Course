# Function (independent)
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))   # Output: Hello, Alice


# Method (inside a class)
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):   # method
        return f"Hello, {self.name}"

p = Person("Bob")
print(p.greet())   # Output: Hello, Bob
