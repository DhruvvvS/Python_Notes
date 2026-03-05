# LEARNING OOPS

# Object -- A "bundle" of related attributes (variables) and methods (functions)
#           EX. phone, book, cup. object can be real life

#           Attributes - are variable created for an object
# FOR EXAMPLE
# we can create many variable/attribute for an object

# FOR phone:-
#           version = 13
#           is_on = True

# FOR book:-
#           title = "The Secret"
#           author = "Rhonda Bryne"
#           page = 280

# FOR cup:-
#           liquid = "chai"
#           temp = 93

#           Method - are function that belongs to an object
# FOR EXAMPLE
# we can create multiple method within an object to use them

# FOR phone:-
#           def turn_on():
#           def turn_off():
#           def make_call():
#           def receive_call():

# FOR book:-
#           def open_book():
#           def read():
#           def close_book():

# FOR cup:-
#           def drink():
#           def fill():
# This is are some example of methods for any object

# CLASS :- blueprint used to design structure and layout of an object

class Car:

  # This is called CONSTRUCTOR method. We need this to construct the object
  # dunder = double underscore
  def __init__(self, model, year, color, for_sale):
    self.model = model        # attribute
    self.year = year          # attribute
    self.color = color        # attribute
    self.for_sale = for_sale  # attribute

  def drive(self):       # METHOD
    print("This " + self.model + " is driving")

  def stop(self):        # METHOD
    print("This " + self.model + " is stopped")

car1 = Car("Toyota", 2022, "Red", True)
car2 = Car("Honda", 2021, "Blue", True)
car3 = Car("Tesla", 2023, "Black", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

car1.drive()
car1.stop()

car2.drive()
car2.stop()

# INSTANCE VARIABLES :- defined inside the constructor method

# CLASS VARIABLES :- shared among all instance(object) of a class
#                    It is defined outside of the constructor method
#                    Allows you to share data among all the objects that are created from that class

class Student:
  school_name = "ABC School"

  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

student1 = Student("John", 15, "10th")

print(student1.school_name)
print(student1.name)
print(Student.school_name)