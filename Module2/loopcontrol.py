#Loop control statements
#Loop control statements change the execution from its normal sequence.
#When execution leaves a scope, all automatic objects that were created in that scope are destroyed.
#The most common loop control statements in Python are break, continue, and pass.

#Break Statement
#The break statement is used to exit a loop prematurely when a certain condition is met.(prematurely means before the loop
#has finished all its iterations)
#When the break statement is encountered inside a loop,
#the loop is immediately terminated, and the program continues with the next statement after the loop.
"""
for letter in "JARVIS":
    if letter == "V":
        break  # This will exit the loop when the letter is "V"
    print("Current Letter:", letter)
print("Out of the loop")

#You can also use the break statement in a while loop.
a1 = int(input("Enter your value: "))
while a1 > 0:
    print("The value are: ", a1)
    a1 -= 1 # This is equivalent to a1 = a1 - 1
    if a1 <= 10:
        break # This will exit the loop when a1 is 10
print("Out of the loop")
"""
#Continue Statement
#The continue statement is used to skip the current iteration of a loop and move on to the next iteration.
#When the continue statement is encountered inside a loop,
#the rest of the code inside the loop for that iteration is skipped, and the loop continues with the next iteration.

for letter in "JARVIS":
    if letter == "V":
        continue  # This will skip the rest of the code when the letter is "V"
    print("Current Letter:", letter)
print("Out of the loop")
"""
a1 = int(input("Enter your value: "))
while a1 > 0:
    a1 -= 1  # This is equivalent to a1 = a1 - 1
    if a1 == 10:
        continue  # This will skip the value of the code when a1 is 10
    print("The value are: ", a1)
print("Out of the loop")"""

#Pass Statement
#The pass statement is a null statement that does nothing.
#It is used when a statement is syntactically required but you do not want to execute any code.
#syntactically required means that the code structure requires a statement to be present, even if it doesn't perform any action.
#The pass statement is often used as a placeholder for code that will be added later or to create empty functions or classes.

for letter1 in "Python":
    if letter1 == "h":
        pass  # This will do nothing when the letter is "h"
        print("This is pass statement")
    print("Current Letter:", letter1)
print("Out of the loop")