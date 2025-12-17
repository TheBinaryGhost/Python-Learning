#Write a program to input two numbers from the user and
#check it's and integer or not using Try and Except block.
'''try:
    a = int(input(" Enter the value of A: "))
    b = int(input(" Enter the value of B: "))
    if isinstance(a, int) and isinstance(b, int):
        print(" Both A and B are integers")
except ValueError:
    print(" Please enter valid integers")'''

#Write a program to input a string from the user evaluate using Try and Except block.
'''try:
    s = input(" Enter a string: ")
    result = eval(s)
    print(" The evaluated result is: ", result)
except Exception as e:
    print(" Exception occurred: ", e)'''

#Write a program to input two number from the user and check its an integer
# or not using Try and Except block, if number are integer then print the sum of that number
# using finally block.
'''sum = None
try:
    a = int(input(" Enter the value of A: "))
    b = int(input(" Enter the value of B: "))
    sum = a + b
except ValueError:
    print(" Please enter valid integers")
finally:
    if sum is not None:
        print(f" The sum is: {sum}")
    print(" Execution completed")'''


#Write a program to input two number from the user and handle
#your exception using else.
'''try:
    a = int(input(" Enter the value of A: "))
    b = int(input(" Enter the value of B: "))
except ValueError:
    print(" Please enter valid integers")
else:
    print(" The number are: ", a, " and ", b)'''

#Write a program to print multiple except block.
try:
    a = int(input(" Enter the value of A: "))
    b = int(input(" Enter the value of B: "))
    c = a / b
    print(" The value of C is: ", c)
except ValueError:
    print(" Please enter valid integers")
except ZeroDivisionError:
    print(" Division by zero is not allowed")