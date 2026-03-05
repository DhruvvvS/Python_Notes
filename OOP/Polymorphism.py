# Polymorphism = Greek word that means "have many forms or faces"
#                poly = Many, morphe = Form

# TWO WAYS to achieve polymorphism
# 1. Inheritance - An object could be treated of the same type as a parent class

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Pizza(Circle):
    def __init__(self, radius):
        super().__init__(radius)

shapes = [Circle(5),Square(8),Pizza(6)]

for shape in shapes:
    print(f"{shape.area()}cm²")

# 2. Duck Typing - the type of object is not checked.
#                  If an object has the required method, it can be used.
#                  “If it looks like a duck and quacks like a duck, it’s a duck.”

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())

# make_sound() does not check whether the object is Dog or Cat.
# It only checks if the object has a sound() method.