# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Create a class
class User:
    #Provide a constructor that runs every time an instance of this class is made
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    #create methods associated with this class
    def greeting(self):
        print(f'Hi. My name is {self.name} and I am {self.age}.')

#Extend a class
class Customer(User):
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0 #Add a default value for a new property in this class

    #Set the balance property if one is provided, using a method
    def set_balance(self, balance):
        self.balance = balance

    def customer_greeting(self):
        print(f'Hi. My name is {self.name}. I am {self. age}. My balance is {self.balance}.')

#Instatiate the User class
anne = User('Anne Wanjiku', 'anne@gmail.com', 30)

#Instantiate the Customer class
steven = Customer('Steven Mwaura', 'steven@yahoo.com', 80)

anne.greeting()
steven.greeting() #A class extension has access to the methods present in its parent
steven.customer_greeting() #It can overwrite the methods in its parent using its own methods
steven.set_balance(200) #Set an explicit balance in the class extension
steven.customer_greeting() #Print the updated class instance

