#If you want to execute something after the loop has finished, you can also use the else statement. 
#The else statement will execute after the loop has finished, unless the loop was terminated by a break statement.

for nums in range(1, 11, 2):
    print(num)
else:
    print('Done!')

num = 0

while num < 10:
    print(num)
    num += 2
    break #Used to break out of the loop, so the else statement will not execute.
else:
    print('Done!')
