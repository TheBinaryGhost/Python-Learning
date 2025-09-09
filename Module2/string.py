#Strings in python
# Strings are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# Strings are collection of character


# Single quote in string
print('Hello, World!')

# Double quote in string
print("Hello, World!")

# Triple quotes in string
print('''Hello, World!''')

#Multiline string
a = """Python is the greatest language and chatgpt is best AI tool.
I love to learn new things about Ethical Hacking and Python programming language.""" #multiline string starts with triple quotes
print(a)

#Update string
a1 = 'Hello, world'
print(a1)
print('Updated string:', a1[:6] + 'Python')

#String slicing
a2 = "Ethical Hacking"
print("index 1 : ", a2[3]) #accessing character at index 3

#Access the value between index 0 to 6
print("index 0 to 6 : ", a2[0:7])

#Access the value till 6
print("index till 6 : ", a2[:9])

#Access the last value from string
print("last index : ", a2[-1])


#String in-built methods

#Capitalize(): Converts the first character to upper case
a3 = "hello, world"
X = a3.capitalize()
print(X)

#Casefold(): Converts string into lower case
a4 = "Hello, World!"
Y = a4.casefold()
print(Y)

#Center(): Returns a centered string
a5 = "hello"
Z = a5.center(20)
print(Z)

#Count(): Returns the number of times a specified value occurs in a string
a6 = "Hello, welcome to my world."
B = a6.count("o")
print(B)


#Encode(): Returns an encoded version of the string
a7 = "Hello, World!"
C = a7.encode()
print(type(C))

#Endswith(): Returns true if the string ends with the specified value
a8 = "Hello, welcome to my world."
D = a8.endswith("world.")
print(D)

#String comparison
#string comparison means comparing two or more strings to determine their relative order or equality.
#In Python, string comparison is done using comparison operators such as ==, !=, <, >, <=, and >=.
#When comparing strings, Python compares them lexicographically, which means it compares the Unicode code
#points of each character in the strings.
#lexicographically means dictionary order
#For example, the string "apple" is considered less than the string "banana" because
#the Unicode code point of the first character 'a' in "apple" is
#less than the Unicode code point of the first character 'b' in "banana".

str1 = "apple"
str2 = "banana"
result = str1 == str2
print(result) #False

str3 = "apple"
result1 = str1 == str3
print(result1) #True

str4 = "A"
str5 = "B"
result2 = str4 > str5
print(result2) #False
