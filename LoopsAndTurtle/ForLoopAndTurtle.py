import turtle # Importing the turtle module
#Creates a turtle that moves in a repeating pattern and draw lines on the screen.

#Functions for a turtle to move in a square pattern and draw lines on the screen.
turtle.speed(1) # Setting the speed of the turtle
turtle.color('blue') # Setting the color of the turtle to blue
turtle.forward(100) # Moving the turtle forward by 100 units
turtle.right(90) # Turning the turtle right by 90 degrees
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90) # Turning the turtle left by 90 degrees

#We are repeating two lines of code here, i.e, moving forward and turning right. We can use a loop to repeat these actions instead of writing them multiple times.
#Using a for loop to do the same thing

turtle.reset() # Resetting the turtle to start fresh
turtle.speed(1) # Setting the speed of the turtle
turtle.color('red') # Setting the color of the turtle to red

for steps in range(4): # Looping 4 times to create a square
    turtle.forward(100) # Moving the turtle forward by 100 units
    turtle.right(90) # Turning the turtle right by 90 degrees

#for loop is best to use when you know the number of iterations in advance.
#Syntax: for variable in range(start, stop, step):
#            statements
#range decides the number of iterations in the loop.
#It can take one, two, or three arguments. If one argument is provided, it is treated as the stop value, and the start value defaults to 0. If two arguments are provided, they are treated as the start and stop values. If three arguments are provided, they are treated as the start, stop, and step values.

turtle.reset() # Resetting the turtle to start fresh
turtle.speed(1) # Setting the speed of the turtle
turtle.color('green') # Setting the color of the turtle to green
for i in range(4):
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)

turtle.done() # Finish the turtle graphics