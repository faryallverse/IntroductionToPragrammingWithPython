def writeToFile(fileName, data):
    accessMode = 'w'
    myFile = open(fileName, accessMode)
    myFile.write(data)
    myFile.close()
    return

fileName = input('Enter the name of your file: ')
data = input('Enter what you want to write in the file: ')

writeToFile(fileName, data)