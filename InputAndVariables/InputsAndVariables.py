#Python is a strictly case-sensitive language. (For efficiency, treat every programming language as if it's case-sensitive.)

#Taking input from the user and storing it in a variable
#The 'input' function allows you to specify a message to display and returns the value typed in by the user.
#We use a variable to remember the value entered by the user.
#Syntax: variableName = input('text')
name = input('What is your name? ')

#Printing the value stored in the variable
#Syntax: print(variableName)
print(name)

#Variable is like a box where you can store something and come back to it later. It's a placeholder.

#Changing the value of name
name = 'Marie'
print(name)

#Rules for naming a variable: 1)Can't have spaces 2)Case-sensitive 3)Cannot start with a number
#Guidelines for naming a variable: 1)Should be descriptive but not too long 2)Use a casing scheme (camelCasing or PacalCasing)

#Connecting string and variables
firstName = input('What is your first name? \n ')
lastName = input('What is your last name? \n ')
print('Hey, ' + firstName + ' ' + lastName)

#Manipulating the contents of a variable
message = 'Hello World'
print(message) #Prints whatever is stored in the variable exactly
print(message.lower()) #Prints whatever is stored in lowercase
print(message.upper()) #Prints whatever is stored in uppercase
print(message.swapcase()) #Prints whatever is stored in a way that lowecased letters swap to uppercase and vice-versa
print(message.find('World')) #Prints the index of the first character of the word 'World' in the string stored
print(message.replace('World', 'Universe')) #Prints the string stored but replaces the word 'World' with 'Universe'
print(message.count('l')) #Prints the number of times the letter 'l' appears in the string stored
print(message.capitalize()) #Prints the string stored but capitalizes the first letter of the string

#The pop-up that appears when visual studio can predict what function, etc. you are going to use and gives you some options for, is called 'IntelliSense'.
