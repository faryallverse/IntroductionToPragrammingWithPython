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

print('Example 1')

#num1 = float(input('Enter the first number: '))
#num2 = float(input('Enter the second number: '))

try: 
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    #By moving the input statements inside the try block,
    #we can also tell the users if they enter a value that cannot be converted to float.

    result = num1/num2

    print('\n', num1, ' / ', num2, ' = %.2f' % result)

except ZeroDivisionError:
    print('\nThe answer is infinity.')
    #Instead of getting the error information from the sys function, we just identified the error.
    #And told the user what we want to tell.

except:
    #Just in case there are errors other than the ZeroDivisionError.
    error = sys.exc_info() [1]
    print('\nSorry! something went wrong.')
    print(error)

finally:
    print('\nYou used our program.')

print('\nExample 2')

#Forcing my program to exit if an error occurs 
#Use fucntion sys.exit()

try:
    n1 = int(input('\nEnter a number: '))
    n2 = int(input('Enter another number: '))
    result = n1/n2
    print('\n', n1, ' / ', n2, ' = ', result)
except ZeroDivisionError:
    print('\nThe answer is infinity.')
    sys.exit() #Will only exit if there's a zero division error.
    print('\nErrorrrrrrrr!!1!') #This will not print because we have exited the program.
except:
    error = sys.exc_info() [1]
    print('\nSorry! something went wrong.')
    print(error)
    sys.exit() #Will exit if there are any errors other than zero division error.
    print('ERORRRRR!!!') #Will not print.
print('\nYou used our program.') #This will also not print because we have exited the program.

#If there are errors, not even the examples after it will run because we have exited the progam.

print('\nExample 3')

#Difference between a finally statement and a simple statement without indentation after except

try:
    n1 = int(input('\nEnter a number: '))
    n2 = int(input('Enter another number: '))
    result = n1/n2
    print('\n', n1, ' / ', n2, ' = %.2f' % result)
except ZeroDivisionError:
    print('\nThe answer is infinity.')
    sys.exit()
    print('\nErrorrrrrrrr!!1!') #This will not print because we have exited the program.
except:
    error = sys.exc_info() [1]
    print('\nSorry! something went wrong.')
    print(error)
    sys.exit() #Will exit if there are any errors other than zero division error.
    print('ERORRRRR!!!') #Will not print.
finally:
    print('\nYou used our program.') #This will print.

#If there are errors, not even the examples after it will run because we have exited the progam.

print('\nExample 4')

#You can also use variables and an if statement to control what happens after an error.
try: 
    n1 = int(input('Enter a number: '))
    n2 = int(input('Enter a number: '))
    r = n1/n2
    print(r)
    errorFlag = False
except ZeroDivisionError:
    print('Infinityyyy!')
    errorFlag = True
except:
    error = sys.exc_info() [1]
    print('\nSorry! something went wrong.')
    print(error)
    errorFlag = True
if not errorFlag:
    print('\nNo errors occured.')
print('\nYou used our program.')

#List of standard Python errors
# https://docs.python.org/3/c-api/exceptions.html#standard-exceptions