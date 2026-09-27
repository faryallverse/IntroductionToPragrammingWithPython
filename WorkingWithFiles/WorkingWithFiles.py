#One of the ways a program can make a note of something is to write it to a file.
#How do you write to a file?
#Use the open function to create and open a file.
#Syntax: open(filename, accessMode)
#You must specify 1)file name 2)access mode
#File Name: The file name is the name of your file including the extension. (data.txt, mytimes.csv)
#The file will be created in the same folder as your program unless you specify a different path.

#The Access Mode specifies what you want to do with the file after you open it.
#Common access modes are:
# 'w': write mode (overwrites existing content)
# 'a': append mode (adds to existing content)
# 'r': read mode (reads existing content) (Default mode if not specified)
# 'b': binary mode (used for binary/non-text files)
# 'r+': read and write mode (allows both reading and writing)
# 'x': exclusive creation mode (creates a new file, fails if the file already exists)
# 'w+': write and read mode (overwrites existing content and allows reading)
# 'a+': append and read mode (adds to existing content and allows reading)

fileName = 'data.txt'  # Specifying the file name
accessMode = 'w'  # Specifying the access mode
myFile = open(fileName, accessMode)  # Opening the file with the specified name and mode

#Writing to the file: Use the write function to write content to the file.
myFile.write ('Hey there!')
myFile.write ('\nHow y\'all doin\'?')
myFile.write ('\nProbably good I believe.')

#Closing the file: After writing to the file, it is important to close it to ensure that all data is properly saved and resources are released.
myFile.close()

print('Contents written to the file successfully.')

#csv (Character Seperated Valus) File: A csv file contains data seperated by a character (usually a comma).
#Each row represents one record of data.
#Makes itself an excel file

filename = 'family.csv'
access = 'w'
file = open(filename, access)

file.write ('Name, Age')
file.write ('\nSarfraz, 60')
file.write ('\nRahat, 58')
file.write ('\nAiny, 31')
file.write ('\nIqra, 30')
file.write ('\nZahid, 27')
file.write ('\nFaryal, 18')

file.close()

#Taking input from user

File = 'user.txt'
Access = 'a'

data = input('Write in your file:')

Myy = open(File, Access)

Myy.write (data)

Myy.close()
