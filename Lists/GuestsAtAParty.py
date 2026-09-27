#Creating an empty list to store the names of the guests
guests = []

#The user doesn't know exactly how many guests are coming to the party, so we will use while loop.
i = 0 
while i != -1:
    #Asking user to enter the names of the guests repeatedly until they reach their total
    name = input('Enter the name of guest no. {} (Enter -1 to finish): '.format(i + 1)).capitalize()
    if name == '-1':
        break
    #Adding the names of the guests to the list
    guests.append(name)
    i += 1

#Sorting the list of guests in alphabetical order
guests.sort()

#Printing the names of the guests in alphabetical order
print('\nThe guests at your party are: ')
for i in guests:
    print(i)