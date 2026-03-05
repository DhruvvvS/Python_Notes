# PROPERTY DECORATOR @property = The @property decorator in Python lets you define methods that are accessed like attributes
#                                   giving you control over getting, setting, and deleting values.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

c = Circle(5)
print(c.radius)   # 5  — calls the getter
c.radius = 10     # calls the setter
del c.radius      # calls the deleter

# DECORATORS = A decorator is a function that wraps another function (or class) to extend or modify its behavior — without changing its source code.

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()
# Before
# Hello!
# After

# The key insight: decorators are just higher-order functions — they take a function and return a (usually enhanced) function.

# EXCEPTION HANDLING = An event that interrupts flow of program   
#                      Exception handling lets you gracefully respond to errors at runtime instead of crashing.
  

# TYPES OF COMMON ERROR
"""       Exception                     Raised When
    
   &    ValueError            Right type, wrong value — int("abc")
   &    TypeError                 Wrong type — "a" + 1
        KeyError                Dict key not found — d["missing"]
        IndexError                 List index out of range
        AttributeError             Attribute doesn't exist
        FileNotFoundError           File doesn't exist
   &    ZeroDivisionError           Division by zero
        ImportError                 Module not found
        StopIteration               Iterator exhausted
        RecursionError          Max recursion depth exceeded
        MemoryError                     Out of memory                                       """

# 1. try: Any code that might cause any error we place it in a try block
#         FOR EX. user input is written in try block as user can type in anything

# 2. except "Nameoferror": Subsequentially following try block we write except block
#                          if we run into any that type of error we can run that particular block of code
#    Some might except Exception which is too broad and covers all types of errors rather than writing it manually

# 3. finally: this block of code will get eeccuted under any of the condition 
#             great use case for file handling
#             ALWAYS runs, exception or not
# Use finally for cleanup (closing files, releasing locks).
# Use else for code that should only run on success.
 
try:
    num = int(input("Enter a number: "))
    print(1/num)

except ZeroDivisionError:
    print("You cannot divide a number by zero!")

except ValueError:
    print("Kindly enter a number.")

except Exception:
    print("Something went wrong!!!")

finally:
    print("This is more helpful in file handling.")

# 4. raise = raise is used to trigger an exception manually — either a new one, or one that's already been caught.

# FORMS OF RAISE

# a. Raise a new exception

# SYNTAX -- raise ExceptionType("message")

# examples
raise ValueError("Age must be positive")
raise TypeError("Expected a string")
raise RuntimeError("Something went wrong")

# b. Raise with no arguments - re-raise current exception

try:
    risky()
except ValueError:
    log("error occurred")
    raise          # re-raises the same ValueError, preserving traceback

# c. Raising from another exception - exception chaining

try:
    connect_to_db()
except ConnectionError as e:
    raise RuntimeError("Service unavailable") from e

# d. Raise from None - suppresssing the original exception

try:
    value = d["key"]
except KeyError:
    raise ValueError("Key not found") from None
# hides the KeyError, only shows ValueError