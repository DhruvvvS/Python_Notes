# Typecasting = Process of converting data type of a variable to another data type
#               str(), int(), float(), bool() this are the functions we will use to typecast
name = "Book"
age = 19
price = 25.99
is_book = True

print(f"Data type is {type(name),type(age),type(price),type(is_book)}")

price = int(price)
is_book = str(is_book)
print(price,is_book) 
print(type(is_book))

# Here price float number is typecasted to integer to show just 25 

#### SPECIAL POINT : To get this sign "²" 1. Make sure numlock is ON 2. alt+0178 

##### INPUT FUNCTION
# input() :- function jo user se input leta hai kisi bhi chiz ka 
#            Returns the entered data as string

name = input ("What is your name : ")
age = input ("What is your age : ")
# yaha input function name aur age ka input le raha hai
# age =+ 1
# this will not run as whenever we store a user input we store it in a form of string.
# soo first we will need to typecast it to integer
age = int(age)
age += 1
# We could also typecast the variable at input only
# LIKE, age = int(input ("What is your age : "))
print(f"Your name is {name}")
print("HAPPY BIRTHDAY!!")
print(f"You are {age} years old")


# "//" FLOOR DIVISION OPERATOR :- it works same as normal division but it rounds up to lowest near integer
# EXAMPLE 
x = 7//2
print(x)

# this will give 3 as floor division operator rounded up 3.5 to 3
# on normal division it would show 3.5