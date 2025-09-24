#write a program to accept a list from the user
#and print the alternate elements of the list
#list1 = input("Enter the list elements separated by space: ").split()
#print("The alternate elements in the list are:", list1[::2])

#Write a program to remove the element "3" from the given list
# list2 = [1, 2, 3, 4, 5, 5, 6]
list2 = [1, 2, 3, 4, 5, 5, 6]
print(list2)
list2.remove(3)
print("The list after removing 3 is:", list2)

#Write a program to insert the element "Python" on index 2
#in the given list
list3 = ["Java", "Php", ".Net", "Angular"]
print("Original list:", list3)
list3.insert(2, "Python")
print("List after inserting Python at index 2:", list3)

#Write a program to add element in list using for loop
"""list4 = []
n = int(input("Enter number of elements you want to add in the list: "))
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    list4.append(element)
print("The elements in the list are:", list4)"""

#Write a program to perfrom slicing with given tuple
#("Python", 1,2,3, "Java", 'A', 'B') with following slicing point:
# - print alternate value of tuple
# - print value between index 1 to 5
# - print the last value of tuple
tuple1 = ("Python", 1, 2, 3, "Java", 'A', 'B')
print("Original tuple:", tuple1)
print("Alternate values in the tuple:", tuple1[::2])
print("Values between index 1 to 5:", tuple1[1:6])
print("Last value in the tuple:", tuple1[-1])

#Write a program to count element in given tuple (1,2,3,4,5,6,7,8).
tuple2 = (1,2,3,4,5,6,7,8)
print("Original tuple:", tuple2)
print("Length of the tuple is:", len(tuple2))

#Write a program to convert tuple into list
x = list(tuple2)
print("Tuple converted to list:", x)

#Write a program to convert two given list into dictionary.
# Listx = [1,2,3,4], Listy =['A', 'B', 'C', 'D']
listx = [1,2,3,4]
listy = ['A', 'B', 'C', 'D']
dict1 = dict(zip(listx, listy))
print("Dictionary created from two lists:", dict1)

#Write a proggram to print keys from the given dictionary {1:"Apple", 2:"Banana", 3:"Grapes"}
# and print keys into list
dict2 = {1:"Apple", 2:"Banana", 3:"Grapes"}
print("Original dictionary:", dict2)
keys = dict2.keys()
print("Keys in the dictionary:", keys)
l1 = list(keys)
print("Keys in the list:", l1)

#Write a program to print values from the given dictionary {1:"Apple", 2:"Banana", 3:"Grapes"}
# and print values into list
values = dict2.values()
print("Values in the dictionary:", values)
l2 = list(values)
print("Values in the list:", l2)

#Suppose d = {"john": 40, "peter": 45}. To obtain the number of entries
# in dictionary which command do we use?
d = {"john": 40, "peter": 45}
print("Number of entries in the dictionary:", len(d))

l2 = [3, 5, 25, 1, 3]
min(l2)
print(min(l2))