# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Angela'
age = 12

#To concatenate a different data type to an str
print('Hi, my name is ' + name + ' and I am ' + str(age))

# String Formatting
#Using positional arguments
print('Hello, my name is {name} and I am {age}.'.format(name = name, age = age))

#Using f-strings
print(f'How are you? My name is {name} and I am {age}.')

# String Methods

s = 'hello world'
#Capitalize a sentence
print(s.capitalize())

#Make all the letters uppercase
print(s.upper())

#Make all the letters lowercase
print(s.lower())

#Swap case
print(s.swapcase())

#Get the length of a string
print(len(s))

#Replace one thing with another
print(s.replace('world', 'everyone'))

#Count
substr = 'h'
print(s.count(substr))

#Starts with returns a boolean
print(s.startswith('hello'))

#Ends with returns a boolean
print(s.endswith('r'))

#Change a string into an array by passing a separator. An empty string to separate into single characters is not working though...
print(s.split())

#Find the index/position of. Returns the 1st index if the argument appears more than once
print(s.find('o'))

#Check if a string is all alpha-numeric returns a bool
print(s.isalnum())

#Check if a string is all alphabetic returns a bool
print(s.isalpha())

#Check if a string is all numeric returns a bool
print(s.isnumeric())
