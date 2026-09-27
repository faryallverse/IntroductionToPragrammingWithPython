#if-else statements allow you to execute different blocks of code based on certain conditions.
#Syntax: if condition:
#            statement(s) #Executed if the condition is true
#       else:
#            statement(s) #Executed if the condition is false

total = int(input('Enter the amount of your purchase: '))
if total > 5000:
    print('You get a free chocolate!')
else: 
    print('You get a free candy!')
print('Have a nice day!')

#Boolean variables are True or False. They are often used in conditional statements to control the flow of a program.
#Boolean variable is often called a flag. It can be used to indicate whether a certain condition has been met or not.

#Initializing a boolean variable is considered good practice.
freeChocolate = False
amount = int(input('Enter the amount of your purchase: '))
if amount > 5000:
    freeChocolate = True
else:
    freeChocolate = False

if freeChocolate: 
    print('You get a free chocolate!') #If freeChocolate is True, then this block of code will be executed.
else:
    print('You get a free candy!')

