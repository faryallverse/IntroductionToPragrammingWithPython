#Taking user input
loan = input('Enter your loan amount: ')
interestRate = input('Enter your interest rate(in percentage): ')
years = input('Enter the number of years for your loan: ')

#Changing the data type of my variables
l = int(loan)
i = float(interestRate)/100
n = int(years)*12

monthlyPayment = l*(i*(1+i)**n)/((1+i)**(n-1))

print('The monthly payment for your loan is %.2f' % monthlyPayment)