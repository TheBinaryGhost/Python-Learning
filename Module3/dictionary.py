# Dictionary
# It is a collection of key and value pair and does not allow duplicate keys.
# It is unordered, changeable and indexed.
# It is mutable, meaning we can change, add or remove items after the dictionary is created.
# It is defined by enclosing elements in curly braces {}.
# It have immutable data type as key and any data type as value.

# Creating a Dictionary
d1 = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'grapes'} #dictionary with integer keys and string values
print(d1)
d2 = {'name': 'John', 'age': 25, 'city': 'New York'} #dictionary with string keys and mixed values
print(d2)

#List into Dictionary Store
d3 = {1: "Apple", 2: "Java", "Fruit": ["Mango", "Banana", "Orange"], "Vegetables": ["Carrot", "Potato", "Cabbage"]}
print(d3)

#Tuple into Dictionary Store
d4 = {1: "Apple", 2: "Java", "Fruit": ("Mango", "Banana", "Orange"), "Vegetables": ("Carrot", "Potato", "Cabbage")}
print(d4)

#Accessing value of dictionary
#Using key inside square brackets []
print("Value for key 2 in d1:", d1[2]) #accessing value using key
print("Value for key 'name' in d2:", d2['name']) #accessing value using key
print("Value for key 'Fruit' in d3:", d3['Fruit']) #accessing list value using key
x = d4[1] #accessing tuple value using key
print(x)

#Using get() method to access value
d1.get(3) #accessing value using get() method
print(d1.get(3))
y = d2.get('name')
print(y)

#Using items() method to get key-value pairs
z = d3.items() #returns a view object that displays a list of a dictionary's key-value tuple pairs
print(z)

#Access the keys using keys() method
k = d1.keys() #returns a view object that displays a list of all the keys in the dictionary
print("The keys are:",k)

#Access the values using values() method
v = d1.values() #returns a view object that displays a list of all the values in the dictionary.
print("The values are:",v)

#Changing value in dictionary
d1[2] = 'blueberry' #changing value for key 2
print("Updated d1:", d1)

#Using update() method to change value
d1.update({3: 'kiwi'}) #updating value for key 3
print(d1)

#Removing item from dictionary
#Using pop() method
d1.pop(4) #removing item with key 4
print("d1 after removing key 4:", d1)
d2.pop('name') #removing item with key 'name'
print("d2 after removing key 'name':", d2)

#Using popitem() method to remove last inserted item
d3.popitem() #removes the last inserted key-value pair
print("d3 after removing last inserted item:", d3)

#Using del keyword to remove item
del d1[1] #removing item with key 1
print("d1 after deleting key 1:", d1)

#Using clear() method to empty the dictionary
d2.clear() #removes all items from the dictionary
print("d2 after clearing all items:", d2)
