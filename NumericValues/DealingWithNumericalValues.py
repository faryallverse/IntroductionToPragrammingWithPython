#Storing numeric values in variables

width = 10
height = 27
#Performing calculations with variables
area = width * height
#Printing the result
print('The area of the rectangle is:', area)
#You cannot concatenate a string and a number, so instead of using the plus sign, you can use a comma to separate the string and the number in the print statement. This will automatically convert the number to a string and print it along with the other text.
#If you want to use the + sign, you need to convert the number area into string, i.e,
print('The area of the rectangle is: ' + str(area)) 
#You could also use format specifier, i.e,
print('The area of the rectangle is: %d' % area)
#%d is basically a placeholder for a decimal integer. The % operator is used to format the string and replace the placeholder with the value of area.

#Arithmetic operations
#Addition: +, Subtraction: -, Multiplication: *, Division: /, Modulus: %, Exponentiation: **
#Floor Division: // returns the largest whole number less than or equal to the division result
#Order of operations: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction (PEMDAS)

l = 2.534
w = 19
a = l * w
print(a)

#Format specifiers are used to format the output of a string. They are placeholders that are replaced with values when the string is printed. The most common format specifiers are:
# %d: decimal integer (%3d means your value needs a width of 3 spaces but where there are no digits, there will be an empty space; %03d means you need 3 spaces of width for your value but where there are no digits, there will be a zero)
# %f: floating-point number (No. of decimal places you need: %.2f)
# %s: string
print('%.2f' % a)
print('%5d' % area)
print('%05d' % area)
#Multiple values/variables in a line
print('The values are %3d, %d, %1.2f.' % (7, area, a))

#Another way to format numbers
print('The area is {0:d}'.format(area))
print('The area is {0:5d}'.format(area))
print('The area is {0:05d}'.format(area))
print('The other area is {0:f}'.format(a))
print('The other area is {0:.2f}'.format(a))
#If you need to print more than one value/variable in a sentece, use the following syntax. The 0,1,2 represents the index numbers of the values/variables.
print('The values are {0:d}, {2:.2f}, {1:2d}'.format(area,7,a))

#Sometimes commands are too long to fit on a single line. You can use a '\' called line continuation character, to indicate a commands continues on the next line.
marks = 10 + 455 + 8666 - 9773 \
    + 7655 - 98777
print(marks)
