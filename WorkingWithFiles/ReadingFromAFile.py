fileName = 'user.txt'
acessMode = 'r'

myFile = open(fileName, acessMode)

content = myFile.read()

print(content)

#Reading one line at a time: readline()

name = 'family.csv'
access = 'r'

myy = open(name, access)

data = myy.readline()
dad = myy.readline()

print('\n', data)
print(dad)

myy.close()