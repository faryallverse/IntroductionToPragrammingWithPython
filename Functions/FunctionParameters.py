#A Parameter is a specialized variable for a function.
#It is going to store a value.
#It is a piece of data passed into a function.

def printMessage(message):  # message is the parameter.
    print(message)
    return

printMessage('Hello World!')

#Multiple Parameters (Seperated by commas)

def greetings(msg, name):
    message = msg + ',' + name + '!'
    return message

print (greetings('Hey there', 'Louis'))