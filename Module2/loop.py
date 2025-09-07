#Looping statements
#So first of all what is looping statement?
#Looping statements in Python are used to execute a block of code repeatedly for a certain number
#of times or until a specific condition is met.
#Loop control statements change execution from its normal sequence.
#When execution leaves a scope, all automatic objects that were created in that scope are destroyed.
#The most common looping statements in Python are for and while loops.

#While Loop
#while loop is an entry-controlled loop that executes a block of code as long as a specified condition is true.
#The syntax of a while loop in Python is as follows:

"""sum = 0
n = int(input("Enter your value: "))
while n > 0:
    sum =  sum + n
    n -= 1  # This is equivalent to n = n - 1
    print("The sum are: ", sum)
print("Out of the loop")"""
#In this example, the while loop will continue to execute as long as the value of n is greater than 0.
#Inside the loop, we add the value of n to the sum variable and then decrement n by 1.
#When n becomes 0, the condition n > 0 will evaluate to false, and the loop will terminate.
#Finally, we print the total sum of all the numbers entered by the user.
#Note: Be careful when using while loops, as they can potentially create infinite loops if the condition never becomes false.
#To avoid infinite loops, make sure to include a way to exit the loop, such as decrementing a counter variable or using a break statement.
#Also, Python provides a break statement that can be used to exit a loop prematurely when a certain condition is met.


#While loop with else
#In Python, a while loop can also have an else clause that is executed when the loop condition becomes false.
#The syntax of a while loop with an else clause is as follows:

"""sum = 0
n = int(input("Enter your value: "))
while n > 0:
    sum =  sum + n
    n -= 1  # This is equivalent to n = n - 1
    print("The sum are: ", sum)
else:
    print("Error loop") #This will execute when the loop condition becomes false.
print("Out of the loop") """

#For loop
#A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable object.
#Iteration means going through each item in the sequence one by one.
#The syntax of a for loop in Python is as follows:

word = ["Python", "Java", "Ethical Hacking"]
for i in word:
    print("The iteration word are: ", i)
    print("The length of the word:", i, '=', len(i))
#In this example, the for loop will iterate over each item in the word list and print it to the console.
#The loop variable i takes on the value of each item in the list one by one,
#and the loop continues until all items in the list have been processed.
#You can also use the range() function to generate a sequence of numbers to iterate over.
#For example:
"""for i in range(5):  # This will iterate over the numbers 0 to 4
    print("The iteration number are: ", i)

a1 = int(input("Enter your value: "))
for i in range(a1):
    print("The iteration number are: ", i)
print("Out of the loop")"""

#Nested for loop
#A nested for loop is a loop that is contained within another loop.
#The inner loop will be executed for each iteration of the outer loop.
#it uses range() function to generate a sequence of numbers to iterate over.
#range(start, stop, step)
#start: The starting value of the sequence (inclusive). Default is 0.
#stop: The ending value of the sequence (exclusive).
#step: The increment (or decrement) between each number in the sequence. Default is 1.

for i in range (1,7): #outer loop
    for j in range (i): #inner loop
        print("*", end=" ")
    print()  # Move to the next line after each row is printed
#In this example, the outer loop iterates over the numbers 1 to 6,
#and for each iteration of the outer loop, the inner loop iterates over the range of the current value of i.
#The inner loop prints asterisks (*) equal to the current value of i, creating a right-angled triangle pattern.
#The end=" " parameter in the print() function is used to print the asterisks on the same line with a space in between.
#The print() function without any arguments is used to move to the next line after each row is printed.

for i in range (6,0,-1): #outer loop
    for j in range (i): #inner loo
        print("*", end=" ")
    print()  # Move to the next line after each row is printed
#In this example, the outer loop iterates over the numbers 6 to 1 in reverse order,
#and for each iteration of the outer loop, the inner loop iterates over the range of the current value of i.

