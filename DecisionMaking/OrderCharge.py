#Calculating the total to charge for an order from an online store in Canada

#Taking user input
total = float(input('Enter your order total: '))
country = input('Enter the country you live in: ').lower()

charge = 0.00

#Charging taxes based on conditions
if country == 'canada':
    province = input('Enter the province of Canada you live in: ').lower()
    if province == 'alberta':
        print('\nCharging 5% General Sales Tax!')
        charge = total + (total*.05)
    elif province == 'ontario' or province == 'new brunswick' or province == 'nova scoatia':
        print('\nCharging 13% Harmonized Sales Tax!')
        charge = total + (total*.13)
    else: 
        print('\nCharging 6% Provincial Sales Tax and 5% General Sales Tax!')
        charge = total + (total*.06 + total*.05)
else:
    print('\nNo tax charged!')
    charge = total

#Printing the final charge
print('\nYour total charge for the order is %.2f.' % charge)
print('\nThankyou for shopping with us!\n')