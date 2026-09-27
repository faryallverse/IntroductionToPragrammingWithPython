fileName = 'myGuests.csv'
accessMode = 'w'

file = open(fileName, accessMode)

file.write ('Anusha, clg')
file.write ('\nRameen, clg')
file.write ('\nAyesha, clg')
file.write ('\nZainab, clg')
file.write ('\nHaniya, uni')
file.write ('\nSharmeen, uni')
file.write ('\nRimsha, gghs')
file.write ('\nWajeeha, gghs')
file.write ('\nIzzah, tkd')
file.write ('\nZaryab,tkd')

file.close()

import csv

aM = 'r'
 
myy = open(fileName, aM)

data = csv.reader(myy)

for row in data:
    print(row)
    print(':'.join(row))
    for value in row:
        print(value)
    print('\n')
myy.close()