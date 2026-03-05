# WHILE LOOP : executes some code WHILE some condition is true
num = int(input("Enter any no. "))
while num <= 0 or num > 20:
    print(f"{num} is out of reach")
    num = int(input("Enter the number again "))

print(f"Your number is {num}")

# FOR LOOP : executes a block of code fixed number of times.
#            you can iterate over range, string, sequence etc.
# FORMAT --> for (any character) in range(to start from, to end at)
# second number in range function is exclusive

for i in range(1, 11):
    print(i)
# This will print no.s from 1 to 10

for x in reversed(range(1, 11)):
    print(x)
# This will print no.s from 10 to 1 in reversed order

# for loops also have step like in indexing
for x in reversed(range(1, 11, 3)):
    print(x)
# This will give no.s in reversed order with 3 steps

# we can iterate over string too in for loop
credit = "1234-5678-9012-3456"
for a in credit:
    print(a)

## CONTINUE KEYWORD : skips over any single iteration
## BREAK KEYWORD : breaks out of the loop
for c in range(1, 21):
    if c == 13:
        continue
    else:
        print(c)

## NESTED LOOP : a loop within another loop
#                outer loop:
#                   inner loop:

for x in range(3):
    for y in range(1, 11):
        print(y, end="")  # this end function gets all the numbers in one line
    print()  # this print in outer loop iterates over next line
