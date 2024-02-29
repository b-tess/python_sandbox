# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#Create a dictionary
#Literal declaration
    #NOTE: The keys are all string literals in this declaration method
person = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 50
}
print('1.', person, type(person))

#Using a constructor
    #NOTE: Here, the keys are NOT string literals
person2 = dict(first_name = 'Jessie', last_name = 'Joe', age = 4)
print('2.', person2, type(person2))

#Get a value in a dict
print('3.', person['first_name']) #dot notation is NOT used to access a dict bracket notation is
print('4.', person.get('last_name')) #Another way to access a dictionary's values

#Add a key/value to a dict
person['phone'] = +254_700123456
print('5.', person)

#Get the keys in a dict
print('6.', person.keys()) #6. dict_keys(['first_name', 'last_name', 'age', 'phone'])
print(type(person.keys())) #<class 'dict_keys'> Which data type is this?

#Get the values in a dict
print('7.', person2.values()) #7. dict_values(['Jessie', 'Joe', 4])
print(type(person2.values())) #<class 'dict_values'>

#Get the items in a dict
print('8.', person2.items()) #8. dict_items([('first_name', 'Jessie'), ('last_name', 'Joe'), ('age', 4)])
print(type(person2.items())) #<class 'dict_items'>

#Make a copy of a dict. Similar to the spread operator in my lovely JS
person3 = person.copy()
person3['city'] = 'Nairobi' #Add to the newly created copy
print('New dict:', person3)

#Remove an item
del(person3['phone'])
age = person3.pop('age') #Returns the value of the key that's been deleted/removed
print('After removal of some items:', person3)
print('Return value of pop from a dict:', age) 

#Clear a dict
person3.clear() #Clears the data in the dict leaving it empty with a length of 0
print('Cleared dict:', person3)

#A list of dicts
people = [
    {'name': 'Alex', 'age': 20},
    {'name': 'Angela', 'age': 70}
]

#Access a value in a list of dicts
print('9.', people[1]['name'])


#The copy method returns a shallow copy. I wanted to check if that means that nested dictionaries are not copied over using the method. They are copied over even when using the spread operator in JS.
#I'm not sure where I got the idea that shallow copies mean that nested data is not copied...
person4 = {
    'name': 'Random',
    'details': {
        'age': 100,
        'city': 'Random City'
    }
}

person5 = person4.copy()
print('Test of copy method:', person5)