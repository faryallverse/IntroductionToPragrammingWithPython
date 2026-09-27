# and: To execute, both conditions need to be true
# or: To execute, only one of the conditions need to be true

age = int(input('Enter your age: '))
grad = input('Have you graduated (yes/no): ').upper()

if age >= 18 and grad == 'YES':
    print('You are eligible to appear for the exam.')
else:
    print('You are not eligible to appear for the exam.')

country = input('What\'s your country? ').lower()
if country == 'bangladesh' or country == 'india' or country == 'pakistan':
    print('Yes, you used to be a part of the Subcontinent.')
else:
    print('No, you were not a part of the Subcontinent.')


#You can also combine and-or in a single statement.
#Order of precedence: 1) and 2) or

subject = input('What\'s your favourite subject dude? ').lower()
major = input('What\'s your major dude? ').lower()
#Case scenarios where I want the print statement to run: 1)Arts and Science 2)Arts and Maths
# if subject == 'arts'and major == 'science'\
#    or major == 'maths': #Because of the precedence, if I write my conditions like this, it's gonna print the meesage if my major is maths without caring what my subject is. To sort this, we use paranthesis.
if subject == 'arts' and (major == 'science' or major == 'maths'):
    print('You should try having a major related to arts dude.')

#We could solve this problem by using booleans too. 