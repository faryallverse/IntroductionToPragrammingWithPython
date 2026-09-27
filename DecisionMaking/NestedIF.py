#You can nest if statements inside each other

day = input('What\'s the day today? ').lower()
coffee = input('Do you have a coffee? (yes/no) ').lower()

if day == 'monday':
    if coffee == 'no':
        print('Go get a coffee dude!') #Gonna execute if it's monday and you don't have a coffee.
    print('Stay fresh for the whole week dude.') #Gonna execute if it's a monday. Does'nt care about coffee.
print('Have a nice day dude!') #Gonna execute all the time. Cares about neither monday nor coffee.