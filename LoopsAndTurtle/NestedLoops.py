#Nesting a loop means having a loop inside another loop. 
#The "inner loop" will be executed one time for each iteration of the "outer loop".

#Using a variable to decide the number of iterations in the loop.
nbr = int(input("Enter the number of iterations: "))

import turtle

turtle.reset()
turtle.speed(5)
turtle.color('red')

for z in range(nbr):
    turtle.forward(50)
    turtle.right(360/nbr)
    for a in range(nbr):
        turtle.forward(25)
        turtle.right(360/nbr)
turtle.done()