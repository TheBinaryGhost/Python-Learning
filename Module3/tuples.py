#Tuples
# A tuple is a collection of items that is ordered and unchangeable.
#It stores data in a sequential manner.
#Tuples are immutable, meaning their elements cannot be changed after the tuple is created.
#Tuples are defined by enclosing elements in parentheses ().
#Stores multiple data types like string, integer, float, boolean, etc.
#Works on zero-based indexing and can contain duplicate elements.
#Tuples are static, meaning their size cannot be changed after creation.
#Tuples are generally faster than lists due to their immutability.

#Creating a Tuple
t1 = (1,2,3,4,5) #this tuple store integer values
t2 = ('apple', 'banana', 'cherry') #this tuple store string values

t3 = (1,2,3,3,4,5,6,'apple','banana','ram',6.5,7.0) #tuple with duplicate values
print("Integer tuple:",t1)
print("String tuple:",t2)
print("Tuple with duplicate values:",t3)

#Checking length of tuple
print("Length of tuple t3:", len(t3))

#Indexing/slicing in tuple
print("First element of tuple t3:", t3[0]) #accessing first element
print("Last element of tuple t3:", t3[-1]) #accessing last element
print("Slicing tuple t3 from index 2 to 5:", t3[2:5]) #slicing from index 2 to 5 (5 is excluded)
print("Index till index 4:", t3[:4]) #slicing from start to index 4 (4 is excluded)

#Converting tuple to list
t4 = list(t3) #converting tuple t3 to list
print("Tuple t3 converted to list:", t4)

#Tuple Constructor
t5 = tuple((10,20,30,40,'mango','grape')) #using tuple() constructor
print("Tuple using constructor:",t5)
t6 = list(t5) #converting tuple t5 to list
print("Tuple t5 converted to list:", t6)

#Adding item but after converting tuple to list
t7 = ('BMW', 'Audi', 'Mercedes', 'Toyota')
print("Original tuple t7:", t7)
print(type(t7))
t8 = list(t7) #converting tuple t7 to list
print("Converted list t8:", t8)
print(type(t8))
t8[2] = 'Porsche' #modifying element at index 2
t9 = tuple(t8) #converting back to tuple
print("Updated tuple t9 after modification:", t9)

#Using loop in tuple
t10 = ('red', 'green', 'blue', 'yellow')
for i in t10:
    print(i)

#Using while loop in tuple
t11 = ('cat', 'dog', 'rabbit', 'hamster')
i = 0
while i < len(t11):
    print(t11[i])
    i = i + 1 #incrementing i to avoid infinite loop
else:
    print("End of tuple")

#Comparing Tuples
t12 = (1,2,3)
t13 = (1,2,4)
print(t12 < t13) #compares if t12 is less than t13
print(t12 > t13) #compares if t12 is greater than t13
print(t12 == t13)