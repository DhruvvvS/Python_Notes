#### MATHEMATICAL FUNCTIONS ####

# MODULO(%) : gives the remainder of the function
number = 10
remainder = number % 3
print (remainder)

x = 3.14
y = 3
z = -4

# ROUND FUNCTIONS round() : Round off the number to nearest integer
result = round(x)
print(result)

# ABSOLUTE VALUE abs() : this function measures the distance of the number from 0 as whole number. 
#                        Converts negative to positive
result = abs(z)
print(result)

# POWER FUNCTION pow() : this function raises the power of the base to the given exponent
result = pow(y,4)
print(result)

# MAXIMUM AND MINIMUM FUNCTIONS max(),min() : 
# max gives the maximum value from the given input
# min gives the minimum value from the given input
result = max(x,y,z)
print(result)
result = min(x,y,z)
print(result)

#### TO GET MATHEMATICAL CONSTANTS ####
# 1st : Import math (import math) library to access math constant 
# 2nd : write math.constant to get that constant
# EX - math.pi will give value of pi(3.14)

import math
print(math.pi)
print(math.e)

# CEIL FUNCTION (math.ceil): rounds up the number to ahead number
a = 2.3
result = math.ceil(a)
print(result)

# FLOOR FUNCTION (math.floor): rounds up the number to behind number
result = math.floor(a)
print(result)