# if = do and work the given snippet of code only IF the condition for it is TRUE
#      ELSE do something else

income = float(input("Enter the money you are earning :"))
if income >= 800000:
    print("You will have to pay tax")
elif income <= 0:
    print("Paisa kama bhai")
else:
    print("Tax free enjoy ;)")

# Also we have ELSE IF (elif) statement to make sure if there are more than 3 conditionns to be checked
# You can add as many elif as you want

# Use of if else with boolean

is_open = True
if is_open:
    print("aaja bhai")
else:
    print("kal aana")


# MATCH STATEMENT : match case statement are same as switch cases in C
#                   it helps reducing use of many elif statement
# case _ : is the default case

x = int(input("enter a number : "))

match x:
    case 1:
        print("Number is one.")
    case 2:
        print("Number is two.")
    case _ :
        print("Number is neither 1 nor 2.")