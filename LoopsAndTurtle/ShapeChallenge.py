#Asking the user to input the shape they want to draw
sides = int(input("Enter the number of sides of the shape you want to draw (3,5,7,etc.): "))
color = input("Enter the color of the shape you want to draw: ").lower()
double = input("Do you want to draw the shape inside the main shape? (yes/no): ").lower()

import turtle

turtle.speed(2)
turtle.color(color)

for steps in range(sides):
    turtle.forward(100)
    turtle.right(360/sides)
    if double == 'yes':
        for inner in range(sides):
            turtle.forward(50)
            turtle.right(360/sides)
turtle.done()