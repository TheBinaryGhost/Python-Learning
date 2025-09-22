#List
# A list is a collection of items in a particular order.
#It stores data in a sequential manner.
#Lists are mutable, meaning their elements can be changed after the list is created.
#Lists are defined by enclosing elements in square brackets [].
#Stores multiple data types like string, integer, float, boolean, etc.
#Works on zero-based indexing and can contain duplicate elements.
#Lists are dynamic, meaning they can grow and shrink in size as needed.

#Creating a List
l1 = [1,2,3,4,5] #this list store integer values
l2 = ['apple', 'banana', 'cherry'] #this list store string values

print("Integer list:",l1)
print("String list:",l2)

#Duplicate values in list
l3 = [1,2,2,3,4,4,5]
print("List with duplicate values:",l3)

#List Constructor
l4 = list((6,7,8,9,10,'apple','mango')) #using list() constructor
print("List using constructor:",l4)

#List Slicing
print("Slicing list of l3 from index 1 to 4:", l3[1:4]) #slicing from index 1 to 4 (4 is excluded)
print("Slicing till index 5:", l3[:5]) #slicing from start to index 5 (5 is excluded)
print("Slicing last value from index -1:", l3[-1]) #slicing last value using negative indexing

#List item change
l5 = ['ram', 'shyam', 'hari', 'sita', 'gita']
print("Original list l5:", l5)

l5[1:3] = ['sonu','pravin','dinesh'] #changing value at index 1
print("Updated list l5:", l5)

#Insert into list
l5.insert(3, 'rahul') #inserting value at index 3
print("List after insertion:", l5)

#Extend list
l6 = ['a', 'b', 'c', 'd', 'e']
l7 = [1, 2, 3]
#l6.extend(l7) #extending l6 with l7
print("Extended list l6:", l6)

#Remove from list
l6.remove('b') #removing value 'b' from list
print("List after removing 'b':", l6)

#Using pop() to remove last item
l6.pop() #removing last item
print("List after popping last item:", l6)

#Using del to remove item at specific index
del l6[0] #deleting item at index 0
print("List after deleting item at index 0:", l6)

#Clear method to empty the list
l6.clear() #clearing the list
print("List after clearing all items:", l6)