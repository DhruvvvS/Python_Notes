# Reading files 

# 1. txt file = plain text file
# We can read the contents of a txt file using the open() function in read mode ('r').
file_path = "example.txt"
with open(file_path, 'r') as file: 
    content = file.read()
    print(content)
    
# 2. Json file = JavaScript Object Notation file, it is made of key-value pairs.
# We can read JSON data from a file using the json module in Python.
import json
with open("example.json", "r") as file:
    json_data = json.load(file)
    print(json_data)
# The json.load() function is used to read JSON data from a file.

# We can also access the value of a particular key in the JSON data using the key name.
print(json_data["name"])  # Output: John Doe
print(json_data["age"])   # Output: 30  

# 3. CSV file = Comma Separated Values file, it is a plain text file that contains data in a tabular format.
# We can read CSV data from a file using the csv module in Python.
import csv
with open("example.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
    for i in csv_reader:
        print(i[1])  # Output: Age (assuming the second column is Age)

# The csv.reader() function is used to read CSV data from a file. It returns an iterable object that can be used to iterate over the rows of the CSV file. Each row is returned as a list of strings.
# printing directly the csv_reader object will give us the memory address but not the actual content of the file.
# In the above code, we are using a for loop to iterate over the rows of the CSV file and print each row.

# We can also use the csv.DictReader() function to read CSV data into a dictionary format, where the keys are the column names and the values are the corresponding cell values.
with open("example.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

# We can also access the value of a particular column in the CSV data, we can give it index or the column name.
print(row["Name"])  # Output: John Doe