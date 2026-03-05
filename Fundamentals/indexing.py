# indexing = accessing elements in string of a sequence using [] (indexing ooperator)
#            [start : end : stop]

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # will show value of "1" according to indexing
print(credit_number[0:5]) # OR print(credit_number[:5]) 5 defines the end point of the indexing
print(credit_number[5:9])
print(credit_number[5:]) # python will assume we will need it till end of the string
print(credit_number[-1]) # to get access of elements in reversed order(from behind)
print(credit_number[::2]) # 2 is written in step block means it will give every character at 2 steps

# Reverse the string
credit_number = credit_number[::-1]
print (credit_number)