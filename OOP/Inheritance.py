# INHERITANCE :- Allows a class to inheriit attributes and methods from another class
#                helps with code reusability
#                class Child(Parent)
#            aka class Sub(Super)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.eat()
dog.sleep()
dog.speak()

cat.eat()
cat.sleep()
cat.speak() 

# MULTIPLE INHERITANCE -- inherit from more than one class
#                         C(A,B)

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Flyer:
    def fly(self):
        print("Flying!")

    def breathe(self):
        print("Breathing in air")


class FlyingFish(Animal, Flyer):
# here multiple inheritance is used as FlyingFish is calling two different parent classes at same time
    def speak(self):
        print("...")
    
fish = FlyingFish("Goldy")
fish.eat()
fish.fly()
fish.breathe()

# MULTILEVEL INHERITANCE -- inherit from a parent class which inherits from a another parent (grandparent for first) class
#                           A -> B(A) -> C(B)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} started")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving")


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def charge(self):
        print(f"Charging {self.battery}kWh battery")

# Here ElectricCar is inheriting from Car and Car class is inheriting from Vehicle class
car = ElectricCar("Tesla", "Model 3", 75)

car.start()
car.drive()
car.charge()

# super() -- Function used in a child class(Sub class) to call methods from a parent class(Super class)
#            Allow you to extend the functionality of the inherited methods
# class Super:
#       pass
# class Sub(Super):
#       pass

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)

s = Student("Rahul", 101)
s.display()