#Operators in python.
#Operators are used to perform operations on variables and values.
#There are different types of operators in python.
#1. Arithmetic Operators
#Arithmetic operators are those operators that perform arithmetic operations on variables and values.
#Example: Addition(+), Subtraction(-), Multiplication(*), Division(/), Modulus(%), Exponentiation(**), Floor Division(//), Increment (++), Decrement (--)
x = 10
y = 20
z = x + y
print("The sum of x and y is:", z)
print(type(z))

x1 = 10
x2 = 20
x3 = x1 * x2
x4 = float(x3)
print(x4)
print(type(x4))


#2. Comparison Operators
#Comparison operators are those operators that compare two values and return a boolean result.
#Example: Equal to(==), Not equal to(!=), Greater than(>), Less than(<), Greater than or equal to(>=), Less than or equal to(<=)
#1. Equal to Equal to
x6 = 5
x7 = 5
x8 = 10
print(x6 == x7)
print(x6 == x8)

#2. Not Equal to
print(x6 != x7)
print(x6 != x8)

#3. Greater than
print(x6 > x7)
print(x6 > x8)

#4. Less than
print(x6 < x7)
print(x6 < x8)

#5. Greater than or equal to
print(x6 >= x7)
print(x6 >= x8)

#6. Less than or equal to
print(x6 <= x7)
print(x6 <= x8)

#3. Logical Operators
#Logical operators are those operators that perform logical operations on boolean values.
#Example: AND(&&), OR(||), NOT(!)
#1. AND
print(x6 > x7 and x6 < x8)

#2. OR
print(x6 > x7 or x6 < x8)

#3. NOT
print(not(x6 > x7))

#4. Bitwise Operators
#Bitwise operators are those operators that perform bit-level operations on binary numbers.
#Example: AND(&), OR(|), NOT(~), XOR(^), Left Shift(<<), Right Shift(>>)


#5. Assignment Operators
#Assignment operators are those operators that assign values to variables.
#Example: Equal(=), Add and Assign(+=), Subtract and Assign(-=), Multiply and Assign(*=), Divide and Assign(/=), Modulus and Assign(%=), Exponentiate and Assign(**=), Floor Divide and Assign(//=), Bitwise AND and Assign(&=), Bitwise OR and Assign(|=), Bitwise XOR and Assign(^=), Left Shift and Assign(<<=), Right Shift and Assign(>>=)
x5 = 5
print("X :", x5)
x5 += 5  # This is equivalent to x5 = x5 + 5
print("X after += 5 :", x5)


#6. Identity Operators
#Identity operators are those operators that compare the memory locations of two objects.
#Example: is, is not
#1. is
x9 = [1, 2, 3, "Ram"]
x10 = [1, 2, 3, "Ram"]
x11 = x9
print(x9 is x11) #the object is matching so it gives True.
print(x9 is x10) #the object is not matching so it gives False.

#2. is not
print(x9 is not x10) 


#7. Membership Operators
#Membership operators are those operators that test for membership in a sequence (such as strings, lists, or tuples).
#Example: in, not in
#1. in
print("Ram" in x9)
print("Shyam" in x9)

#2. not in
print("Ram" not in x10)
print("Shyam" not in x10)

#operator precedence
#Operator precedence determines the order in which operations are performed in an expression.
#In Python, the order of precedence is as follows (from highest to lowest):
#1. Parentheses
#2. Exponentiation
#3. Unary plus and minus
#4. Multiplication, Division, Floor Division, Modulus
#5. Addition, Subtraction
#6. Bitwise Shift
#7. Bitwise AND
#8. Bitwise XOR
#9. Bitwise OR
#10. Comparison
#11. Identity
#12. Membership
#13. Logical NOT
#14. Logical AND
#15. Logical OR


#8. Operator Precedence
x12 = 20
x13 = 10
x14 = 15
x15 = 5

x16 = (x12 + x13) * x14 / x15  # Parentheses have the highest precedence
print(x16)

x17 = ((x12 + x13) * x14 + 5) / x15  # Parentheses have the highest precedence
x18 = int(x17)  # Convert the result to an integer
print("value of x18:", x18)