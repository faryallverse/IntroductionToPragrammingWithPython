import csv

fileName = 'data.csv'
access = 'w'
file = open(fileName, access)

file.write ('Lahore,Pakistan')
file.write ('\nLos Angeles,USA')
file.write ('\nDubai,UAE')
file.write ('\nMakkah,SaudiArabia')
file.write ('\nManchester,UK')
file.write ('\nMumbai,India')
file.write ('\nIstanbul,Turkey')

file.close()

#Functions from the csv module:

#The reader function will take an open csv file and return each row from the file into a list.
#Syntax: dataFromFile = csv.reader(myCSVfile)
#If your file is not using a comma to seperate the values, you can tell the reader function what character is used as a delimiter.
#Syntax: dataFromFile = csv.reader(myCSVfile, delimiter=';')

accessMode = 'r'
myCSVfile = open(fileName, accessMode)
data = csv.reader(myCSVfile)

for currentRow in data:
    print(currentRow)
    for currentWord in currentRow:
        print(currentWord)

myCSVfile.close()

print('\n')

#You can use the join function to format the output
#Syntax: SeperaterToDisplay.join(myList)

acc = 'r'
csvv = open(fileName, acc)

word = csv.reader(csvv)

for row in word:
    print(': '.join(row))