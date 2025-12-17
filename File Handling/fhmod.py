#write a program to create a .txt file and readn the entire text file.
s = '''Ethical hacking is an art of hacking. In ethical hacking, we hack the system
with the permission of the owner to find vulnerabilities and fix them
before malicious hackers can exploit them.'''
file = open("demo3.txt", "w") # w- write, r- read, a- append
file.write(s)
print("File created and data written successfully.")
file.close()
file = open("demo3.txt", "r")
file_content = file.read()
print(file_content)
file.close()

#write a program to read the first N lines of a file.
file = open("demo3.txt", "r")
file_content = file.read()
print(file_content[:100]) # read first N lines
file.close()

#write a program to append text to file and display the text.
s = "Ethical hacking is a very interesting field."
file = open("demo3.txt", "a") # a- append
file.write(s)
print("Data appended successfully.")
file.close()
file = open("demo3.txt", "r")
file_content = file.read()
print(file_content)
file.close()

#write a program to store given list ["Java",
#"JavaScript", "C", "C++", "Ruby"] into a file and read the file.
P = ["Java", "JavaScript", "C", "C++", "Ruby"]
file = open("demo4.txt", "w")
file.writelines(P) # writelines is used to write a list into file
print("List written to file successfully.")
file = open("demo4.txt", "r")
file_content1 = file.readlines() # readlines is used to read a file into a list
print(file_content1)
file.close()
