#Object Oriented Programming (OOP) in Python
#Python classes provide all the standard features of Object Oriented Programming including
#the class inheritance mechanism allowing multiple base classes, a derived class can
#override any methods of its base class or classes,
#and a method can call the method of a base class with the same name.
#Objects can also contain arbitraryamounts and types of data.

#Creating Class
class myclass:
    x = 5 #class attribute and its property
print(myclass)

#Creating Object
p1 = myclass() #object creation where p1 is object of class myclass
print(p1.x) #accessing class attribute through object

#Calling a function by object
class func:
    def myfun(self): #defining function inside class
        print(" Hello World")
#creating an object of class func
p2 = func()
p2.myfun() #calling function using object

#Creating a constructor
class constructor:
    def __init__(self): #constructor with parameters
        print(" This is a constructor")
#creating an object of class constructor
p3 = constructor() #constructor is called automatically during object creation

#Changing the value by object
class changevalue:
    def __init__(self, name, age):
        self.name = name
        self.age = age #it became variable for the class
    
    def myfun1(self):
        print("My name is: "+ self.name)

#creating an object of class changevalue
p4 = changevalue("JARVIS", 2500)
p4.age
p4.name
#Changing the value of age by object
p4.age = 3000
print("My name is: ", p4.name, "and my age is: ", p4.age)

#Deleting the object
del p4.age
print("Age: ", p4.age) #it will give error because age attribute is deleted