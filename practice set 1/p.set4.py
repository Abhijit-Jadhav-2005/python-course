# Q. write a python program to print the content of a directory using the os module.
# shearch online for the function which does that.

import os

# Specify the directory path
path = "/"

# Get the list of files and directories in the specified directory
dir_contents = os.listdir(path)

# Print the list of files and directories
for item in dir_contents:
    print(item)

