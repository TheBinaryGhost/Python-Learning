# Conditional Statements
#So conditional statement in Python is used to perform different actions based on different conditions depending
#on whether a specific Boolean constraint evaluates to true or false.
#The most common conditional statements in Python are if, elif, and else.
#These statements allow you to control the flow of your program based on certain conditions.


#flow of simple if
#works with only on condition
var = 15
if (var == 15): #condition is getting true
   print("value of variable is 15")
print("Bye")


a = 25
if (a >= 30): #condition is getting false
   print("value of variable is 25")
print("Bye")

#flow of if_else
#works with two conditions
"""a = int(input("Enter the value of a: "))
a1 = int(input("Enter the value of a1: "))
if a<a1: #condition is getting true
   print("a1 is greater")
else: #else part call
   print("a is greater")"""

a2 = 10
a3 = 5
if a2<a3: #condition is getting false
   print("a3 is greater")
else:
   print("a2 is greater") #else part call

#flow of if else ladder
#works with multiple conditions
"""
a4 = int(input("Enter the total marks: "))
if a4 >= 90:
   print("Grade A")
elif a4 >= 80 and a4 < 90:
   print("Grade B")
elif a4 >= 70 and a4 < 80:
   print("Grade C")
elif a4 >= 60 and a4 < 70:
   print("Grade D")
else:
   print("Grade E need to improve")"""


#flow of nested if

a5 = int(input("Enter the age: "))
if a5 >= 18: #outer if
   weg = int(input("Enter the weight: "))
   if weg >= 50: #inner if
       print("You can donate your blood")
   elif weg < 50:
       print("Increase your weight")
else:
   print("You are not eligible to donate blood")