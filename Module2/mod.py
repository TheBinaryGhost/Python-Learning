#Write a program to find whether a given number (accepted from the user)
#is even or odd, and print the message to the user accordingly.


"""a = int(input("Enter the first value: "))
if a % 2 == 0:
    print("The given number is even")
else:
    print("The given number is odd")
"""


#Write a program to find whether a given number (accepted from the user)
#is greater then or less then and print the message to the user accordingly.

"""b = int(input("Enter the first value: "))
c = int(input("Enter the second value: "))
if b > c:
    print("The first number is greater then second number")
elif b < c:
    print("The first number is less then second number")
else:
    print("Both numbers are equal")"""

#Write a program to find out the grade if given percentage value (accepted from the user)
#and print the message according given criteria.
"""percentage = float(input("Enter your percentage: "))
if percentage >= 90:
    print("You have got A+ grade")
elif percentage >= 80:
    print("You have got A grade")
elif percentage >= 70:
    print("You have got B grade")
elif percentage >= 60:
    print("You have got C grade")
else:
    print("You have got D grade")
    print("Note: D grade need to reappear the exam")
"""


#Write a program to generate 1 to 10 using the loop
for i in range(1,11):
    print(i)

#write a program to generate 10 to 1 using the loop
for i in range (10,0,-1):
    print(i)


#write a program to print the following pattern:
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1,7):
    for j in range(i):
        print("*", end=" ")
    print()

#write a program to print following pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range (1,7):
    for j in range(1,i):
        print(j, end=" ")
    print()

#write a program to convert the string "hello python" into uppercase using string built-in function.
a = "hello python"
print(a.upper())

#write a program to convert the string "HELLO PYTHON" into lowercase using string built-in function.
b = "HELLO PYTHON"
print(b.lower())

x = ['ab', 'cd']
for i in x:
    i.upper()
    print(x)