#Whatever and whenever you write code, some things will go wrong in your code.

#Types of Errors in Python:
#1) Syntax 2) Runtime (Exceptions) 3) Logical (Semantic)

#1)Syntax Errors: Violation of Python's grammar rules
#The development tool can detect them.

#2)Runtime Errors: The code passes the syntax check and starts running, but encounters an operation that it cannot legally perform.
#Occur while the program is executing.

#3)Logical Errors: Occur due to flawed code logic, bad math formulas, or incorrect conditional operators.
#The program runs completely without crashing or throwing error messages, but the final output is incorrect.


#A calculator program: Take two numbers and divide them for the user

# num1 = float(input('Enter the first number: '))
# num2 = float(input('Enter the second number: '))

# result = num1/num2

# print(num1, ' / ', num2, ' = %.2f' % result)

#What if the user enters 0 as num2.
#Dividing anything by 0 is something that the program can't perform legally.
#We are gonna use try/except
#try:
#    statements you want the program to try to run
#except:
#       what the programmer should do if the try code doesn't work.

#finally: 
#        block of code that always executes, regardless of whether an exception (error) was raised or caught.

#sys.exc_info() is a function in Python's built-in sys module that returns a tuple containing detailed information about the exception currently being handled.
#sys.exc_info()[0]: The Exception Type (e.g., <class 'ZeroDivisionError'>)
#sys.exc_info()[1]: The Exception Value / Instance (the error message object)
#sys.exc_info()[2]: The Traceback Object (encapsulates the call stack at the error location)

import sys
#Provides access to variables and functions that interact closely with the Python interpreter and runtime environment.

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

try: 
    result = num1/num2
    print(num1, ' / ', num2, ' = %.2f' % result)
except:
    error = sys.exc_info() [1]
    print('Sorry! something went wrong.')
    print(error)
finally:
    print('You used our Divider Calculator.')


#raise: A function you call to intentionally trigger (or throw) your own exceptions and errors.

