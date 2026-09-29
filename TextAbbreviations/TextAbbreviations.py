fileName = 'abbreviations.txt'
accessMode = 'w'

myFile = open(fileName, accessMode)

myFile.write('LOL,Laughing Out Loud\n') #write statement doesn't add a line break like a print statement.
myFile.write('ROTFL,Rolling On The Floor Laughing\n')
myFile.write('BRB,Be Right Back\n')
myFile.write('OMG,Oh My God\n')
myFile.write('IDK,I Don\'t Know\n')
myFile.write('BTW,By The Way\n')
myFile.write('NVM,Never Mind\n')
myFile.write('LMK,Let Me Know\n')
myFile.write('TTYL,Talk To You Later\n')
myFile.write('FYI,For Your Information\n')
myFile.write('SMH,Shaking My Hand\n')
myFile.write('TBH,To Be Honest\n')
myFile.write('FR,For Real\n')
myFile.write('NGL,Not Gonna Lie\n')
myFile.write('OFC,Of Course\n')
myFile.write('RN,Right Now\n')
myFile.write('TMI,Too Much Information\n')
myFile.write('ASAP,As Soon As Possible\n')
myFile.write('ETA,Estimated Time Of Arrival\n')
myFile.write('TBD,To Be Decided\n')

myFile.close()

message = input('Enter your text message: ')

abbreviations = {} #Creates a dictionary
#Dictionary: A data type that stores pairs: a key and the value attached to it.
#You look things up by the key and the value attached is returned. 
#The value attached can never be the key. It only works one way.

try: 
    with open(fileName) as f: #Opens the file as f and 'with' closes it as soon as we are done with try.
        for line in f: #Loops through the file one line at a time
            abrv, full = line.strip().split(',', 1)
            #line.strip(): Removes any stray characters or spaces in the line
            #line.split(',', 1): Cuts the text into two items splitted by ,.
            #The 1 means split only at the first comma. Just in case there are other commas in the abbreviation.
            #abrv, full: Assigning the two items to these variables.
            abbreviations[abrv.upper()] = full #Stores the pair of variables into dictionary
except FileNotFoundError:
    print('abbreviations.txt file not found.')

result = [] #Creating an empty list to store the text word by word
punct = '.,?!;:'

for word in message.split(): #message.split() chops the message into a list of words.
    clean = word.strip(punct) #The punctuation is lost from the message to match with the file.
    #'...LOL!' becomes 'LOL'
    noRight = word.rstrip(punct) #Only cuts the punctuation on the right end of the word.
    #'...LOL!' becomes '...LOL' length = 6
    noLeft = word.lstrip(punct) #Only cuts the punctuation on the left end of the word.
    #'...LOL!' becomes 'LOL!' length = 4
    before = word[:len(word) - len(noLeft)]
    #len(word) = 7, len(noLeft) = 4, 7-4 = 3
    #word[:3]: Everything up to position 3 (...)
    after = word[len(noRight):]
    #len(noRight) = 6
    #word[6:]: Everything from position 6 onwards (!)
    translation = abbreviations.get(clean.upper(), clean)
    #get(key, default): Looks the clean word up in the dictionary.
    #key: To find (clean) [LOL]
    #If the key is found: The value attached to it is returned. [Laughing Out Loud] 
    #default: What to return if the key isn't found (the original word)
    #clean.upper: Capitalizes the whole word as the abbreviations are stored in capital letters in the file.
    result.append(before + translation + after) #Adds the word to the end of the list.
    #before: ... + translation: Laughing Out Loud + after: !
    # = ...Laughing Out Loud!

text = ' '.join(result)
#Glues the words in the list together into one string putting a single space
#(the text in the quotes) between each item.

print(text)
