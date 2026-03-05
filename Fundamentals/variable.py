# variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains


# STRINGS --------- (Always in double coates)

# type 1 :- directly using function
print("Hello Dhruv")

# type 2 :- assigning then function
name = "Dhruv"
print(name)             # Only variable
print("Hello",name)     # some text before variable (comma to seperate variable from string)

# type 3 :- f string (most easy to use)
# FORMAT -- func(f"text{variable}")
food = "Pizza"
print(f"Hello {name}, Do you like {food}")


# INTEGERS -------- 
# age = "19"   (double coates) would technically make it string
age = 19
print(f"I am {age} years old")


# FLOAT --------- Decimal values
price = 25.99
print(f"The price of food is ${price}")


# BOOLEAN --------- True OR False (most use case in IF ELSE)
is_free = False
print(f"Is the pizza for free: {is_free}")