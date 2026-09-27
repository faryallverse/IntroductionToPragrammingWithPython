#List is an abject that allows you to store multiple items in a single variable. 
#Lists are one of the most versatile data structures in Python and can hold items of different data types, including other lists.

#Syntax: nameOfList = [item1, item2, item3]

#You can create an empty list and add values later.
#Syntax: nameOfList = []

#You can reference items in a list by their index(position of the item in the list), which starts at 0 for the first item.
#Syntax: nameOfList[index]

guests = ["John", "Paul", "George", "Ringo"]
print(guests[0])  # Output: John
print(guests[1])  # Output: Paul

#You can even count backwards from the end of the list using negative indexing.
print(guests[-1])  # Output: Ringo
print(guests[-2])  # Output: George
