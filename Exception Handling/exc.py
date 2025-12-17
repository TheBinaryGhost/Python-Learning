# Exception handling is a mechanism in programming languages to handle runtime
# errors gracefully without crashing the program.
# it means the abnormal situation occurs at runtime
# and stop the execution of the program.
# In Python, exception handling is done using the try, except, else, and finally blocks.
# Type of exception: 
# 1. User Define Exception
# In user define exception, user can generate his custom exception in py by inherited the exception class.

# Basic Exception Handling
'''try: #the code which is written try block can be occur error at runtime

    a = int(input(" Enter the value of A: "))
    b = int(input(" Enter the value of B: "))
    c= a/b
    print(" The value of C is: ",c)
except Exception as e: # the code which is written except block will be executed when the exception occurs.
    print(" Exception Occurred: ",e)
print("Bye")'''

# Handling multiple exceptions
'''try:
    print(x)
except NameError:
    print(" Variable x is not defined")
except:
    print("Exception occurred")'''

#Using else with exception
'''try:
    #print("Hello")
    print(x)
except:
    print("Something went wrong")
else:
    print("No error occurred")'''

#Using finally block with exception
# in finally block, the code will be executed no matter exception occurs or not.
'''try:
    #print("Hello")
    print(x)
except:
    print("Something went wrong")
finally:
    print("The finally block is executed")'''

# User Define Exception
class MyException(Exception):
    pass
c = 25
if c > 5:
    raise MyException("Something went wrong")

