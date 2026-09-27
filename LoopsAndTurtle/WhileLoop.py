#When you don't know the number of iterations your loop is gonna make, you use a while loop.
#While loop allows you to repeat a block of code as long as a certain condition is true.
#Syntax: variable = value (variable initialization)
#        while condition:
#            # code block to be executed

answer = '0'
while answer != '4':
    answer = input('What is 2 + 2? ')
print('Correct! 2 + 2 = 4')
#We don't know how many times the user will answer incorrectly, so we use a while loop to keep asking until they get it right.

#Always make sure that your condition will eventually become false, otherwise you will create an infinite loop.
#Always make sure to have a way to break out of the loop, otherwise it will run forever.
