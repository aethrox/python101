# File operation

# file = open('myfiles.txt', 'r') # Read mode > 'r'
# file.close()

# with open('file.txt', 'r') as f:
#     # ALL OF MY CODE
#     pass

# with open('file.txt', 'r') as f:
#     content = f.read()
#     print(content)

# ------

# from time import sleep

# file = open('file.txt', 'w')
# file.write("Hello Visual Code!")
# file.flush() # Pythons print method as an exclusive attribute namely, 
#              # flush which allows the user to decide if he wants his output to be buffered or not.

# with open('file.txt', 'r') as f:
#     content = f.read()
#     print(content)

# sleep(100)

# Python file permissions

"""
r > Only read mode
w > Only write mode
x > Create file mode
a > Append mode
b > Binary mode
+ > This will open a file for reading and writing (Updating)
"""

# from os import *
# from time import sleep

# mkdir('test_directory') # make directory
# chdir('test_directory') # change directory location
# sleep(10) # The program sleeps for 10 seconds.
# rename('test_file.txt', 'new_test.txt') # renaming file
# remove('new_test.txt') # Remove file and directory