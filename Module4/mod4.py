#Create a function that can accept two arguments name and subject and print value of both arguments.
def details(name, subject):
    print("Name:", name)
    print("Subject:", subject)
#Call the function with two values.
details("Alice", "Mathematics")

#Write a function sum() such that it can accept two number arguments and print their sum.
def sum(a, b):
    print("Sum:", a + b)
#Call the function with two numbers.
sum(5, 10)

#Write a function calculation() such that it accept two variables and calculate addition, subtraction, multiplication and division.
'''x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = input("The calculation you want to perform +, -, *, /: ")
def calculation(x, y, z):
    if z == '+':
        print("Addition:", x + y)
    elif z == '-':
        print("Subtraction:", x - y)
    elif z == '*':
        print("Multiplication:", x * y)
    elif z == '/':
        print("Division:", x / y)
    else:
        print("Invalid operation")
calculation(x, y, z)'''

#write a recursive function to calculate the sum of numbers from 0 to 10.
def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)
result = recursive_sum(10)
print("Sum from 0 to 10:", result)

#Create function without any name that can accept two argument and then print sum of its value
sum = lambda a, b: print("Sum using lambda:", a + b)
sum(7, 3)

#Write a program to generate a random number between 1000 to 5000 using python inbuilt module.
import random
random = random.randint(1000, 5000)
print("Random number between 1000 and 5000:", random)

#Write a program to generate a random captcha list, using python inbuilt module.
import random
import string
def generate_captcha(length):
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha
captcha_list = [generate_captcha(8) for _ in range(5)]
print("Random Captcha List:", captcha_list)

#Write a program to shuffle captcha list using python inbuilt module.
import random
captcha_list = ['a1B2c3D4', 'E5f6G7h8', 'I9j0K1l2', 'M3n4O5p6', 'Q7r8S9t0']
random.shuffle(captcha_list)
print("Shuffled Captcha List:", captcha_list)

random.uniform(3,4)
print("Random float between 3 and 4:", random.uniform(3,4))

