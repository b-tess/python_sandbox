# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Initialize a tuple
fruits = ('Apples', 'Bananas', 'Oranges')

#Using the constructor
fruits2 = tuple(('Apples', 'Bananas', 'Oranges'))
print('1.', fruits, fruits2)

#NOTE: If a tuple has only one value in it during initialization, it needs to have a trailing comma for it to be recognized as a tuple
fruits3 = ('Apples')
print('2.', fruits3, type(fruits3)) #Apples <class 'str'>

fruits4 = ('Apples',)
print('3.', fruits4, type(fruits4)) #('Apples',) <class 'tuple'>

#Get an element from a tuple
print('4.', fruits[0])

#A tuple cannot be changed so this will give an error (TypeError)
# fruits2[1] = 'Lemons'
# print('5', fruits2)

#Delete a tuple
# del fruits4
#print('6', fruits4) #This will give a NameError as the fruits4 tuple has been deleted

#Get the length of a tuple
print('Length:', len(fruits))
print('\n')

#Which methods are available for tuples? How does one add to a tuple? How is an empty tuple declared?
 


# A Set is a collection which is unordered and unindexed. No duplicate members.
#Create a Set
fruits_set = {'apples', 'oranges', 'bananas'}
print('1', fruits_set, type(fruits_set)) #1 {'bananas', 'apples', 'oranges'} <class 'set'>

#Using the constructor
fruits_set2 = set() #This initializes an empty set

#Add a value to a set
fruits_set2.add('lemons') #Only one element can be added at a time
fruits_set2.add('watermelons')
print('2', fruits_set2)

#Remove an element from a Set
fruits_set2.remove('lemons')
print('3', fruits_set2)

#Clear all the elements in a Set
fruits_set.clear()
print('4', fruits_set) #This clears the elements and the Set still remains as empty
print('Length:', len(fruits_set))

# print('Index access', fruits_set2[0]) #Since a Set is unindexed, trying to access its elements will give a TypeError. How are the elements of a Set accessed? Is a Set iterable?

#Check if a value is in a Set. This returns a boolean
print('Check if element is present:', 'watermelons' in fruits_set2)

#Is a Set iterable? Yes.
fruits_set3 = {'apples', 'oranges', 'bananas'}
for item in fruits_set3:
    print(item)

#Delete a Set entirely
#del fruits_set
#print('5', fruits_set) #This gives a NameError as fruits_set is no longer defined after deletion
