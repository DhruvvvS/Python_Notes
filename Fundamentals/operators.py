# LOGICAL OPERATORS = evaluate multiple conditions (or, and, not)
#                   or = at least one condition must be true
#                   and = both conditions must be true
#                   not = inverts the condidtion (not True = False, not False = True)


# CONDITIONAL (Ternary) OPERATOR
# conditional expression = One line shortcut for if-else statement
#                          X if condition else Y

a = 5
print("positive" if a>2 else "negative")
result = "even" if a%2==0 else "odd"
print(result)


### STRING INPUT AND ITS FUNCTIONS ###
name = input("Enter your full name: ") # it will store a string input in name variable 

# LENGTH FUNCTION [len()] --> gives us length of the string, will be in integer
# Ex "bro code" = (0,1,2,3,4,5,6,7,8) also includes spaces
result = len(name)
print (result)

# FIND FUNCTION [str.find()] --> finds the first occurence of the given character in the string
# Also string character counting starts from 0 indices as in array.
result = name.find(" ") 
print(result)
#               [str.rfind()] --> finds the last occurence of the given character in the string
# If python is not able to locate any given character it will return "-1" #


# STRING CHANGES FUNCTIONS 

# !  str.capitalize() : capitalize the first character
name = name.capitalize()
print(name)

# ! str.upper() : converts all the string characters in upper case
name = name.upper()
print(name)

# ! str.lower() : converts all the string characters in lower case
name = name.lower()
print(name)

# BOOLEAN STRING FUNCTIONS

# ! str.isdigit() : If string only contains digits it will return True
result = name.isdigit()
print(result)

# ! str.isalpha() : If string only contains alphabetical characters it will return True should not include spaces also
result = name.isalpha()
print(result)


# REPLACE FUNCTION [str.replace(to replace,by)] --> replaces one character by another
name = name.replace("a"," ")
print(name)