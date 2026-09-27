#Decision Making with code

#Everyday we need to make decisions.
#The choice we make depends on different conditons.
#If your code is going to solve problems, it needs to be able to make decisions.

#if statements
#Allow you to specify a block of code to be executed if a condition is true.
#Syntax: if condition:
#             statement(s)

answer = input('Would you like express shipping? (yes/no): ')
if answer == 'yes': # = represents assignment, == represents comparison
    print('That will be an extra 10 rupees.') #indentation is important.

#Relational operators (Used to compare values)
# == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to)

print('Have a nice day!')

favouriteAvenger = input('Who is your favourite Avenger? ')
if favouriteAvenger == 'Iron Man':
    print('Lesgoooooooo!')

#What if someone typed Iron Man not in the exact way we expected? We can use the lower() or upper() method to convert the input to lowercase or uppercase before comparing it.

favouriteSpidey = input('Who is your favourite Spiderman? ')
if favouriteSpidey.upper() == 'ANDREW GARFIELD':
    print('SEMMMM DUDEEEE!')

captain = 'steve rogers'
cap = input('What\'s the name of the first Captain America? ')
if cap.upper() == captain.upper():
    print('Correct! You can do this all day!')

#You can also write it in a way that if a condition is not true, then print this, like this:
number = int(input('Enter a number: '))
if not number == 7: #same as if number != 7
    print('Congratulations! You are safe.')

