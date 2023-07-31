"""
s=open("one",mode='r')
print(s.read())


# Opening a File:
# To start working with a file, you need to open it. Python provides the open() function
# for this purpose. It takes two parameters: the file path and the mode in which you want to
# open the file (e.g., read, write, append, etc.).
# python
# Copy code


file = open("example.txt", "r")  # Opens the file in read mode

#
# Reading from a File:
# Once a file is open in read mode, you can retrieve its contents using various methods.
# The most common method is read(), which reads the entire file as a string.
#
# python
# Copy code


content = file.read()  # Reads the entire file content
print(content)


# You can also read the file line by line using the readline() method:
#
# python
# Copy code


line = file.readline()  # Reads a single line from the file
print(line)


# Writing to a File:
# To write data to a file, you need to open it in write mode or append mode. In write mode,
# the file is overwritten, while in append mode, new data is added at the end of the file.
#
# python
# Copy code

file = open("example.txt", "w")  # Opens the file in write mode
file.write("Hello, World!")  # Writes the given string to the file
file.close()  # Closes the file after writing


# Appending to a File:
# If you want to add data to an existing file without overwriting its contents, open
# it in append mode.
#
# python
# Copy code

file = open("example.txt", "a")  # Opens the file in append mode
file.write("Appending new data!")  # Appends the given string to the file
file.close()  # Closes the file after appending

# Closing a File:
# It's important to close a file once you're done working with it. Closing a file releases
# its resources and ensures that all data is saved.
#
# python
# Copy code

file.close()  # Closes the file


# Error Handling:
# When working with files, errors can occur. To handle them gracefully, you can use a try-except
# block to catch and handle exceptions.

try:
    f = open("1.file001.py", "r")
    # Perform file operations here
except IOError:
    print("An error occurred while opening the file.")
finally:
    f.close()  # Closes the file even if an error occurs


# These are some fundamental file handling features in Python. Remember to always handle errors
# and close files properly to ensure efficient and reliable file operations.
"""


