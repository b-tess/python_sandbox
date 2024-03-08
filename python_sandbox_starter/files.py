# Python has functions for creating, reading, updating, and deleting files.

#Create a file, set its mode and open it
my_file = open('myFile.txt', 'w')

#Get some information on the file using some built-in file object properties
print('Name: ', my_file.name)
print('Is closed: ', my_file.closed)
print('Mode: ', my_file.mode)

#Write into a file
my_file.write('I am learning Python')
my_file.write(' and this experience is making me realize that I like JavaScript more.')
my_file.close() #Close the file