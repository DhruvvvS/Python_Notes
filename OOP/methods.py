# INSTANCE METHOD -- An instance method is a method that belongs to an object of a class.
#                    It can access and modify instance variables using "self".
""" Why self is Important?

    It represents the current object

    Used to access instance variables """

class ClassName:

    def __init__(self): # CONSTRUCTOR METHOD
        pass
    def gajodhar(self): # INSTANCE METHOD
        pass

# Here gajodhar is an instance variable designated with self.

# ABSTRACT METHOD -- An abstract method is a method that is declared but does not contain implementation.
#                    It must be implemented in the child class.
# To create abstract methods, we use the abc module:
# from abc import ABC, abstractmethod

#                   ✔ Abstract method is defined using "@abstractmethod"
#                   ✔ Abstract class must inherit from ABC
#                   ✔ We cannot create object of abstract class
#                   ✔ Child class must implement abstract method

from abc import ABC, abstractmethod

class Shape(ABC):   # Abstract class
    
    @abstractmethod
    def area(self):   # Abstract method
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


c = Circle(5)
print(c.area())



# STATIC METHOD -- method that belongs to a class rather than any object from that class
#                  Best for utility functions that do not need access to class data
#                * Can be called using class name or object
#                * Need decorator before initailising "@staticmethod"
class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance method
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    # Static method
    @staticmethod
    def school_name():
        print("School Name: ABC Public School")


# Creating object
s1 = Student("Rahul", 85)

# Calling instance method
s1.display()

# Calling static method
Student.school_name()

# school_name() → Static Method (does not use "self" or "cls")

# CLASS METHOD -- A class method is a method that works with the class itself, not with individual objects.
#                 Allow operation related to class itself
#               * It takes "cls" as the first parameter
#               * Uses "@classmethod" decorator
#               ✔ Can modify class variables
#               ✔ Can be called using class name

class Student:
    school = "ABC Public School"   # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

    def display(self):
        print("Name:", self.name)
        print("School:", Student.school)


# Before change
s1 = Student("Rahul")
s1.display()

# Changing class variable using class method
Student.change_school("XYZ School")

# After change
s1.display()

# MAGIC METHODS -- aka DUNDER METHODS (dounble underscore) 
#                  They are automatically called by many of Python's in built operations
#                  They allow to define or customize behaviour of objects

class Book:

    # assigning attributes
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # string representation of the object when printing directly into the console
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # checks if two objects are equal
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    # compares lesser than with other object
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    # compares greater than with other object
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    # concatenates the object attributes
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    # contains the string in object
    def __contains__(self, keyword):
        return keyword in self.title or self.author
    
    # gives the item at that particular index
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key '{key}' was not found"
        

book1 = Book("The Secret","Rhonda Byrne",233)
book2 = Book("Harry Potter","JK Rowling",265)    
book3 = Book("Art of War","Sun Tzu",198)
book4 = Book("The Secret","Rhonda Byrne",167)

print(book1) 
# printing only on the basis of __init__ would give memory location of the object and not attributes
# printing with __str__ will print the actual attribute values

print(book1 == book4)
print(book1 < book3)
print(book1 > book4)
print(book2 + book3)
print("The" in book1)

print(book3['title'])
print(book2['author'])
print(book1['num_pages'])
print(book4['audio'])