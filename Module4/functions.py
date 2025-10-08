#Functions in Python
#Function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
#In Python, a function is defined using the def keyword.

#Types of Functions
#1. Built-in Functions
#print(), input(), len(), type(), int(), str(), float(), list(), dict(), set(), tuple(), range(), etc.
print("Hello, World!")  # Built-in function to print to console
length = len("Hello")  # Built-in function to get length of a string
print(length)
for i in range(1,9):
    print(i)  # Built-in function to generate a sequence of numbers

x = round(5.678)  # Built-in function to round a number
print(x)

#2. User-defined Functions
def myfun():
    print("This is a user-defined function")
myfun()  # Calling the user-defined function

#Passing arguments to a function
#Function with one argument
def myfun1(a):
    print("The value of a is:", a)
myfun1(10)  # Calling the function with one argument

#Function with two arguments
def myfun2(a, b):
    print("The value of a is:", a)
    print("The value of b is:", b)
myfun2(10, 20)  # Calling the function with two arguments

#Keyword arguments
def myfun3(child1, child2, child3):
    print("The youngest child is " + child3)
myfun3(child1="Pravin", child2="Sonu", child3="Dinesh")  # Calling the function with keyword arguments


#Default parameter values
def fun4(Province="Madhesh"):
    print("I am from " + Province)
fun4("Gandaki")  # Calling the function with a parameter
fun4("Koshi")  # Calling the function with a parameter
fun4("Bagmati")  # Calling the function with a parameter
fun4()  # Calling the function without a parameter, uses default value


#Passing a list into function
def fun5(fruit):
    for i in fruit:
        print(i)
fruits = ["Mango", "Banana", "Orange"]
fun5(fruits)  # Calling the function with a list


#Return values from a function
def fun6(x):
    return 5 * x
print(fun6(3))  # Calling the function and printing the return value
print(fun6(5))  # Calling the function and printing the return value
print(fun6(9))  # Calling the function and printing the return value

#Recursion in functions
#Recursion is a function that calls itself.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Calling the recursive function to calculate factorial of 5
#num = int(input("Enter a number: "))
# print("Factorial of", num, "is", factorial(num))  # Calling the recursive function with user input


#3. Anonymous Functions (Lambda Functions)
x = lambda a: a + 10
print(x(5))  # Calling the lambda function
y = lambda a, b: a * b
print(y(5, 6))  # Calling the lambda function with two arguments

#Global variabless
#A variable declared outside of a function is a global variable and can be accessed inside a function.
x1 = 25  # Global variable
def myfun7():
    global x1  # Declare x1 as global to modify it
    print(x1)  # Accessing global variable
    x1 = 20  # Modifying global variable
myfun7()  # Calling the function
print(x1)  # Printing modified global variable

#Local variables
#A variable declared inside a function is a local variable and can only be accessed inside that function.
def sum(x,y):
    sum = x + y  # Local variable
    return sum
print("The sum is:",sum(10, 20))  # Calling the function and printing the return value
# print(sum)  # This will raise an error as sum is a local variable
