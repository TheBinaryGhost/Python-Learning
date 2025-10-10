# Random module
# This module provides functions to generate random numbers and perform random selections.
# Random number operation (in-built functions of random module)
# choice() - returns a randomly selected element from a non-empty sequence.
# randrange() - returns a randomly selected element from the specified range.
# randint() - returns a random integer within a specified range.
# shuffle() - shuffles the elements of a list in place.
#from random import choice, randrange, randint, shuffle - to import specific functions from the random module

# Importing choice function from random module
from random import choice
l1 = [1, 2, 3, 4, 5]
print(choice(l1))  # Randomly selects and prints an element from the list l1

# Using randint function from random module
from random import randint
otp = randint(1000, 9999)  # Generates a random integer between 1000 and 9999
print("Your otp is: ", otp)  # Prints the generated OTP

'''Making otp validator
from random import randint
otp = randint(1000, 9999)
print("Your otp is: ", otp)
user_otp = int(input("Enter your otp: "))
if user_otp == otp:
    print("Valid otp")
else:
    print("Invalid otp")'''

# Using shuffle function from random module
from random import shuffle
l2 = ["Apple", "Banana", "Mango", "Grapes"]
x = shuffle(l2)  # Shuffles the list l2 in place
print(l2)  # Prints the shuffled list

