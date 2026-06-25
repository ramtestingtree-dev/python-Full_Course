#Single Inheritance
class Animal:
    def speak(self):
        print("Animal makes sound")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")
dog = Dog()
dog.speak()

# #Multiple Inheritance
class Father:
    def land(self):
        print("Nothing")

class Mother:
    def gold(self):
        print("Full Gold")

class Son(Father, Mother):
    pass
son = Son()
son.land()
son.gold()

# #Multilevel Inheritance
class Grandparent:
    def property(self):
        print("Grandparent: Owns land")

class Parent(Grandparent):
    def property(self):
        print("Parent: Owns house")

class Child(Parent):
    def property(self):
        print("Child: Owns car")
        super().property()              #Super function is used to call the parent method which is overrides
        Grandparent.property(self)

c = Child()
c.property()   # Output: Child: Owns car

#Hybrid Inheritance
class A:
    def feature(self):
        print("Feature from A")

class B(A):
    def feature(self):
        print("Feature from B")

class C(A):
    def feature(self):
        print("Feature from C")

class D(B, C):  # Hybrid: multiple + hierarchical
    def feature(self):
        print("Feature from D")

d = D()
d.feature()   # Output: Feature from D