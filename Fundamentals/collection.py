# COLLECTION --> It is a single "variable" used to store multiple values of same data type
#                SAME AS "ARRAY" IN C LANGUAGE
# Types of collection :-

# LIST = [] , ordered and changeable. Duplicates are OK in it
# SET = {} , unordered and immutable, but ADD and REMOVE can be done. NO duplicates
# TUPLES = () , ordered and unchangeable. Duplicates are OK in it. FASTER from both above

# dir("name of collection") function shows all the function and operations that can be done on collections
# help("name of collection") function explains all the function and operations that can be done on collections


"""x = []
print(help(x))

x = {}
print(help(x))

x = ()
print(help(x))"""

# 2D COLLECTION :- It is a collection made of 1D collection .Collections in 2D works like MATRIX with rows and columns in consideration
# Collection can be made with list in list, tuple in tuple, set in set, set in tuple accordingly 

fruits =     ["orange","banana","apple","pomegranate"]
vegetables = ["spinach","ockra","potato"]
shakes =     ["chocolate","oreo","kitkat","latte"]

groceries = [fruits,vegetables,shakes]
print(groceries)

# to print a particular element in it we have to define by rows and columns works like indexing (starts with zero)
print(groceries[0][2])  # will print apple
print(groceries[1]) # will print entire second row

# using loop to print
for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()


# DICTIONARY :- is a collection of {key:value} pairs
#               it is ordered and changeable collection. NO duplicates are entertained
# key:value can be anything like ID:password, Item:price etc.
# dictionary encloses key value pair in curly braces like in sets and seperates key and value with colon

# creating an example country:capital dictionary

capitals = {"USA":"Washington DC",
            "India":"New Delhi",
            "Russia":"Moscow",
            "Greece":"Athens"}



print(capitals.get("India")) # get function gets the value from the dictionary of the particular key

# if python dictionary does not have the key we want in dictionary then it will return "None"
print(capitals.get("Japan")) # it will return None

# update function adds or changes the key:value pair. It can only accept one arguement
capitals.update({"Italy":"Rome"})
capitals.update({"India":"Mumbai"}) 

print(capitals)

# pop function removes the key with its value from dictionary
capitals.pop("Russia")
print(capitals)

# popitem function deletes the last key value pair from dictionary
capitals.popitem()
print(capitals)

# key function gives all the keys from dictionary
key = capitals.keys()
for key in capitals.keys():
    print(key)

# values function gives all the values from dictionary
value = capitals.values()
for value in capitals.values():
    print(value)

# items function give both key and value pair made up in a 2D List of Tuples
print(capitals.items()) # this willshow 2D collection of tuples in list

for item in capitals.items():
    print(item)

for key , value in capitals.items():
    print(f"{key} : {value}")