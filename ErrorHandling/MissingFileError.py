import sys

fileName = input('Enter the name of the file you want to read: ')
accessMode = 'r'

try:
    myFile = open(fileName, accessMode)
except:
     error = sys.exc_info() [1]
     print(error)