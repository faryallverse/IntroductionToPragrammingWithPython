#I am a comment
#Printing Hello World on the screen
print('Hello World')

#Displaying text: print statement
#Syntax: print('Text') / print("text")
print("The Capybara is the world's largest rodent.")
print('The Capybara likes to live in groups.')
print("The capybara can swim.")
#If there is a single quote or double quote inside your string, choose the other one to enclose it.
#For efficiency, choose one and stick with it.

#Multiple lines: 1) Multiple print statements 2) Escape Sequence Newline (\n) 3) Triple quotes
print('Mai Hoon Na\nA film by Farah Khan')

#When you put the string in triple quotes, it will be displayed the way you have the string in the text editor.
print('''Hickory
Dickory
Dock!''')
print("""A
B C""")
#print("A
#B C") or the same with single quotes will cause an error

#What if there is a single quote and a double quote both in the text?
#Option no.1
print('Here is a double quote " ' + "and here is a single quote ' ")
#String Concatenation: Joining strings with a + sign.
#Option no.2
print('Here is a double quote \" and here is a single quote \'. ')
#Used escape sequences \" and \'.
#If I want something to appear not in the way it normally appears, I can use the \ to make it an escape sequence which escapes the 'traditional' way of printing the thing.
