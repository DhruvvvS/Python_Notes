# FILE DETECTION means detecting whether a file exists or not in the system.
# We can use the os module to detect whether a file exists or not.

import os
# To detect whether a file exists or not, we can use the os.path.exists() function.
file_path = "example.txt"

# We can give file paths in different ways, such as absolute path or relative path.
# Absolute path is the complete path from the root directory to the file, such as "C:\Users\Username\Documents\example.txt".
# Relative path is the path from the current working directory to the file, such as "example.txt" if the file is in the same directory as the script.

# We can also use path module to get some inbuilt files and directories in the system.
from pathlib import Path

# The os.path.exists() function returns True if the file exists, and False if it does not exist.
if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")        
else:
    print(f"The file '{file_path}' does not exist.")

# We can also use the os.path.isfile() function to check if the path is a file.
if os.path.isfile(file_path):
    print(f"The file '{file_path}' is a file.")
else:   
    print(f"The file '{file_path}' is not a file.")

# We can also use the os.path.isdir() function to check if the path is a directory.
if os.path.isdir(file_path):
    print(f"The file '{file_path}' is a directory.")
else:
    print(f"The file '{file_path}' is not a directory.")

# Using pathlib (modern, recommended)
p = Path("file.txt")
print(p.exists())
print(p.is_file())
print(p.is_dir())

# p.suffix will give the file extension
print(p.suffix)