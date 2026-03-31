# Program to demonstrate file handling operations

# Writing to a file
file = open("demo_file.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("This file is created to demonstrate file handling.\n")
file.close()

# Reading the file
file = open("demo_file.txt", "r")
print("File content after writing:")
print(file.read())
file.close()

# Appending to the file
file = open("demo_file.txt", "a")
file.write("This line is added later using append mode.\n")
file.close()

# Reading again after appending
file = open("demo_file.txt", "r")
print("File content after appending:")
print(file.read())
file.close()

print("File handling operations completed successfully.")