#What is file handling?
#File handling is a way to store data in files.
#It allows us to read, write, and manipulate files on our computer using programming languages like python.
# Important part for web applications.

# open ('File name', 'Permission')
'''s= "This is my file handling program"
file = open("demo1.txt", "w") # w- write, r- read, a- append
file.write(s)
print("File created and data written successfully.")
file.close()'''

# File read
'''file = open("demo1.txt", "r")
file_content = file.read()
print(file_content)
file.close()'''

# Write a list into file
'''prem = ["Python", "Ethical Hacking", "Cloud Security", "Machine Learning"]
file = open("demo2.txt", "w")
file.writelines(prem) # writelines is used to write a list into file
print("List written to file successfully.")
file = open("demo2.txt", "r")
file_content1 = file.readlines() # readlines is used to read a file into a list
print(file_content1)
file = open("demo2.txt", "r")
file_content = file.read()
print(file_content)
file.close()'''

# Append the value into file
s = "Python is a programming language."
file = open("demo1.txt", "a") # a- append
file.write(s)
print("Data appended successfully.")
file.close()