#The index() function will search the list and return the index of the position where the value was found.

raftaar = ['Faryal', 'Haniya', 'Sharmeen', 'Maham', 'Zainab', 'Fatima', 'Ahmad', 'Ahmed', 'Roshan', 'Zunnurain']

#I want to find what's the index of Fatima in the list.
print('Fatima is at index number', raftaar.index('Fatima'), '.')

#Printing the values of the list raftaar
for members in raftaar:
    print(members)

#Only the first 5 values of the list raftaar
print('\nThe first 5 values of the list raftaar are:')
for i in range(5):
    print(raftaar[i])

#All the remaining values of the list raftaar
print('\nThe remaining values of the list raftaar are:')
#I can either find the index of the last value of the list raftaar and use it in the range() function
#Or I can use the len() function to find the length of the list raftaar and use it in the range() function.
for i in range(5, len(raftaar)):
    print(raftaar[i])

#Sorting the list in alphabetical order
raftaar.sort()
print('\nThe list raftaar in alphabetical order is:')
for mem in raftaar:
    print(mem)