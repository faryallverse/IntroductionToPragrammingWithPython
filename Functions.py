#One of the problems wuth code is you are frequently doing the same thing over and over again.

#A Function is a reusable block of code with a name that does something. Sometimes called a Method.
#Syntax: def functionName():
#            code
#            return
#Calling the Function:
#functionName()
#Because Python interprets code line by line, you need to define functions before you call it.
#You can also call a function in another function.

def printMsg():
    print('Hey there, F.R.I.E.N.D.S.!')
    return

def main():
    printMsg()
    printNames() #This function is defined later but it's gonna work because it's called in another function, which is in turn called after all the functions are defined.
                 #Thus, ths block of code iss not going to execute unless all the functions are defined.
    return

def printNames():
    names = ['Chandler', 'Monica', 'Pheobe', 'Joey', 'Rachel', 'Ross']
    for name in names:
        print(name)
    return

main()