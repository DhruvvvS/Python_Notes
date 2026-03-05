#  FUNCTION : A block of reusable code
#             place () paranthesis to call it 

# def keyword is used to define and initiate functions

def happy_birthday():
    print("Happy birthday to you!")

happy_birthday()

# here happy_birthday is the name of the function initialised by def keyword 
# and is printed directly without any print statement

# Arguments can be passed in functions and Parameters can be setted up for passing arguments

def happy_birthday(x,y):
    print(f"Happy birthday to {x}")
    print(f"You are {y} years old")

happy_birthday("Shaam", 21)

# here x and y are two parameters and shaam and 21 are arguments passed to both parameters respectively

# This are Positional Arguments that is changing the placing of passing arguments can change the results
happy_birthday(21, "Shaam")


# Return statement : used to end a function 
#                    and send a result back to the caller

def add(x,y):
    z = x + y
    return z

print(add(2,3))

# here functions value is stored in return statement z and that is why it is needed to be printed
# using return statement we can return some data back to the place where we called our function

# In this section we dicussed and learned about positional arguments

# DEFAULT ARGUMENTS : default value assigned for certain parameters which is fixed and will not change
#                     reduces number of arguments and makes function more flexible

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)
print(net_price(500))

# here discount and tax are two default arguments as they are being fixed with a value 
# and now we only need to pass argument for list_price

print(net_price(500,0.1))
# best thing about default argument is also that we can only pass 2 argument and it will work
# now discount value will be the value passed by user than fixed

print(net_price(500,0.1,0))
# now the values will be this passed values

# FACT - non default argument comes ahead of default argument 
# OR default argument comes after non default argument

# KEYWORD ARGUMENT : argument preceded by an identifier
#                    helps in readibility
#                    order of arguments does not matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title}.{first} {last}")

hello("Hello",title="Mr",first="John",last="Wick")
# here title and first and last are made keyword arguments to not get confused in names
# we can change position of arguments and it will work the same

hello("Hello",title="Mr",last="Wick",first="John")
# both will work same

# FACT - positional argument comes ahead of keyword argument 
# OR keyword argument comes after positional argument

for x in range(1,11):
    print(x, end="")
# here end is the keyword argument which is built in print function
print()

# ARBITARY ARGUMENT : to access varying amount of argument 
# i.e. suppose there is function for two variables and three values are passed then it will iterate over each of thosse 3 args passed

# * it is unpacking operator when we use args or kwargs we pack it in tuples and dictionary respectively so * is used to unpack it

# *args :- -> args means arguments 
#          -> allows to pass multiple non key arguments
#          -> packs in TUPLE type
#          -> we can name this different than args after * symbol (Ex. *"nameofargs")

# **kwargs :- -> kwargs means keyword arguments
#             -> allows to pass multiple keyword-arguments
#             -> packs in DICTIONARY type
#             -> we can name this different than kwargs after ** symbol (Ex. **"nameofkwargs")

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(2, 6, 5, 4, 7, 10), flush=True)

def address(**adr):
    for value in adr.values():
        print(value)
    for key in adr.keys():
        print(key)
    for item in adr.items():
        print(item)

address(street= "wallst",
              city= "Mum",
              state= "Mp" ,
              country= "IN" ,
              pocode= "532" )   

# we can use both args and kwargs together
# it always works when args is before kwargs as parameter

def label(*args,**kwargs):
    for arg in args:
        print(arg , end=" ")
    print()
    for kwarg in kwargs.values():
        print(kwarg,end=" ")

label("Dr.","Neil","Nitin","Mukesh",
      street= "wallst",
      city= "Mum",
      state= "Mp" ,
      country= "IN" ,
      pocode= "532" )
print()
# LIST COMPREHENSION : a concise way to create lists in python
#             Format : [expression for value in iterable if condition]

doubles = []
for x in range(1,11):
    doubles.append(x * 2)
print(doubles)

# above code can be written in short using list comprehension

double = [y * 2 for y in range(1,11)]
print(double)