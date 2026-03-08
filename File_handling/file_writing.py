# Writing files

# 1. txt file = plain text file 

txt_data = "This is a plain text file. It can contain any text data, such as letters, numbers, and symbols. It does not support formatting or multimedia content."
# We can write this data to a txt file using the open() function in write mode ('w').

file_path = "example.txt"
with open(file_path, 'w') as file:
    file.write(txt_data)
    print
# The open() function takes two arguments: the file path and the mode. The mode 'w' stands for write mode, which means that if the file already exists, it will be overwritten. If the file does not exist, it will be created.

# We can also use the 'a' mode to append data to the file instead of overwriting it.
with open(file_path, 'a') as file:
    file.write("\nThis line will be appended to the file.")
    print
# The '\n' character is used to add a new line before the appended text.

# We can also write multiple lines to the file using the writelines() method, which takes a list of strings as an argument.
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open(file_path, 'w') as file:
    file.writelines(lines)
    print
# The writelines() method does not add new lines automatically, so we need to include the '\n' character at the end of each line in the list.

""" Mode	                  Meaning
    "w"	    Write (creates file or overwrites existing file)
    "a"	    Append (adds content to the end)
    "x"	    Create file, error if it exists
    "w+"	Read and write (creates file or overwrites existing file)
    "a+"	Read and append (creates file or adds to end)"""

# 2. Json file = JavaScript Object Notation file, it is made of key-value pairs.
# We can write JSON data to a file using the json module in Python.
import json

json_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

with open("example.json", "w") as file:
    json.dump(json_data, file)
    print
# The json.dump() function is used to write JSON data to a file. It takes two arguments: the data to be written and the file object.
# dump function converts the dictionary into a JSON string and writes it to the file.

# it will print the json file in a straight line to ident it properly we can use the indent parameter in the json.dump() function.

with open("example1.json", "w") as file:
    json.dump(json_data, file, indent=4)
    print
# You can see the difference in the output of example.json and example1.json. The indent parameter adds indentation to the JSON data, making it more readable. In this case, we have set the indent to 4 spaces.

"""  json.load()	Read JSON file
    json.loads()	Convert JSON string to Python object  """

# 3. CSV file = Comma Separated Values file, it is a plain text file that contains data in a tabular format, where each line represents a row and each value is separated by a comma.
# We can write CSV data to a file using the csv module in Python.
import csv

csv_data = [
    ["Name", "Age", "City"],    
    ["John Doe", 30, "New York"],
    ["Jane Smith", 25, "Los Angeles"],
    ["Mike Johnson", 35, "Chicago"]
]

with open("example.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
    print("CSV file has been written successfully.")
# The csv.writer() function is used to create a writer object that can write data to a CSV file. 
# The writerows() method is used to write multiple rows of data to the file. Each row is represented as a list of values.
# The newline='' parameter in the open() function is used to prevent adding extra new lines between rows in the CSV file, which can happen on some platforms.