# A List is a collection which is ordered and changeable. Allows duplicate members.
fruits = ['Bananas', 'Apples', 'Raspberries', 'Mangos']

print('1.', fruits)

#Add an element to the end of a list (append)
fruits.append('Lemons')
print('2.', fruits)

#Remove an element from a list
fruits.remove('Bananas')
print('3.', fruits)

#Insert an element at a specific index in a list
fruits.insert(2, 'Bananas')
print('4.', fruits)

#Remove an element from any index with pop. If an argument is not provided, it removes the last element in a list
fruits.pop()
print('5.', fruits)

#Reverse a list
fruits.reverse()
print('6.', fruits)
print(fruits[0])

#Sort a list in ascending order (default)
fruits.sort()
print('7.', fruits)
print(fruits[0])

#Sort a list in descending order
fruits.sort(reverse=True)
print('8.', fruits)
print(fruits[0])