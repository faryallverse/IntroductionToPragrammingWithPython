#Sometimes, there are multiple conditions that need to be checked. In such cases, we can use the elif statement to check for additional conditions after the initial if statement.
#Syntax: if condition1:
#             statement(s) #Executed if the condition is true
#       elif condition2:
#             statement(s) #Executed if condition1 is false and condition2 is true
#       elif conditionN:
#             statement(s) #Executed if condition1, condition2, ..., conditionN-1 are false and conditionN is true
#       else:
#             statement(s) #Executed if all the conditions are false

country = input('Where are you from? ').upper()

if country == 'CANADA':
    print('Hello!')
elif country == 'GERMANY':
    print('Guten Tag!')
elif country == 'FRANCE':
     print('Bonjour!')
elif country == 'SPAIN':
    print('Hola!')
elif country == 'PAKISTAN':
    print('Assalam-o-Alaikum!')
else:
    print('Sorry, langauge not available.')
