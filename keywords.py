 #Keywords in Python
# Keywords are reserved words in Python that have special meaning and cannot be used as variable names.
#and = 5  # This will raise a SyntaxError because 'and' is a keyword
# Other keywords include: False, None, True, as, assert, break, class and etc.
# You can find the complete list of keywords in Python documentation or by using the keyword module.
# Using the keyword module to print all keywords
#help ("keywords")  # This will display all the keywords in Python

#Data types in Python
#Numeric data types: int, float, complex
#Int
#int is those type of data that can hold whole numbers.
a = 10
print(type(a))  # This will print the type of variable a.

#Float data type
#float is those type of data that can hold decimal numbers.
b = 10.5
print(type(b))  # This will print the type of variable b.

#Complex data type
#complex is those type of data that can hold complex numbers.
c = 1 + 2j
print(type(c))  # This will print the type of variable c.


#Boolean data type
#Boolean is those data types that can hold only two values: True or False.
d = True
print(type(d))  # This will print the type of variable d, which is a boolean.

e = False
print(type(e))  # This will print the type of variable e, which is a boolean.

#Set data type
#Set data is those data types that can hold multiple unique values.
f = {a, b, c} #set data type is represented by curly braces with unique elements.
print(type(f))  # This will print the type of variable f, which is a set.

#Dictionary data type
#Dictionary data type is those data types which store data in key-value pairs.
g = {"name": "Python", "version": 3.9} #Dictionary data type is represented by curly braces with key-value pairs.
print(type(g))  # This will print the type of variable g, which is a dictionary.

#Sequence data types
#Sequence data type is those data types that can hold multiple values in an ordered manner.
#it is of three types
#List data type
#this data type is those data types that can hold multiple values in an ordered manner.
h = [1, 2, 3, 4, 5]  #List data type is represented by square brackets with ordered elements.
print(type(h))  # This will print the type of variable h, which is a list.

#String data type
#this data type is those data types that can hold multiple characters in an ordered manner.
h1 = "Hello, Python!"  #String data type is represented by single or double quotes
print(type(h1))  # This will print the type of variable h1, which is a string.

#Tuple data type
#this data type is those data types that can hold multiple values in an ordered manner.
h2 = (1, 2, 3)  #Tuple data type is represented by parentheses with ordered elements.
print(type(h2))  # This will print the type of variable h2, which is a tuple.

x,y,z = ("Meow", "Meow", "Biralo")
print(x, y, z)  # This will print the values of x, y, and z which are unpacked from the tuple.