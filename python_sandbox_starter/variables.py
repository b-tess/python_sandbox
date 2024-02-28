# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

#Variable assignment 
num1 = 3 				#int
num2 = 79.5				#float
name = 'Random'			#str			
is_correct = False    	#Boolean

#Multiple assignment
num3, num4, name1, is_wrong = (3, 79.5, 'Random', True)

#Check the data type of a variable
print(type(name))

#Type cast a variable to a different data type
num4 = int(num4)
print(type(num4))
