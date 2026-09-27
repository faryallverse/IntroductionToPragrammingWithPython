import turtle

length = int(input('Enter the length of the line (or 0 to stop): '))
color = input('What pen color you would like to use? ').lower()
angle = int(input('What angle would you like? (0-360) '))

while length != 0:
    turtle.color(color)
    turtle.forward(length)
    turtle.right(angle)

    length = int(input('Enter the length of the line (or 0 to stop): '))

    if length != 0:
        color = input('What pen color you would like to use? ')
        angle = int(input('What angle would you like? (0-360) '))

print('You are an amazing artist!')