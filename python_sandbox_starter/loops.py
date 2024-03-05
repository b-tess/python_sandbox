# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ['Anne', 'John', 'Bobby', 'Lillian']

#Break
for person in people:
    if person == 'Bobby':
        break
    print(f'Current person in break: {person}')

print('\n')

#Continue
for person in people:
    if person == 'Bobby':
        continue
    print(f'Current person in continue: {person}')

print('\n')

#Range
for number in range(-5, 1):
    print(f'Number = {number}')

# While loops execute a set of statements as long as a condition is true.
str = 'random'
count = 0
while count <= len(str):
    print(f'Count = {count}')
    count += 1
