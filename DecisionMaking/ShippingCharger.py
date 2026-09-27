#Calculating shipping charges for a shopper

#Taking input from the user
total = float(input('Enter the total amount of your purchase: '))

#ShippingCost
shippingCost = 10

#Initializing boolean variable
shippingCharge = False

#Checking the condition for shipping charge
if total < 50:
    shippingCharge = True
    print('Your shipping charge is 10 rupees.')

if shippingCharge:
    final = total + shippingCost
else:
    final = total

#Printing the final total including shipping
print('Your total (including shipping) is %.2f rupees.' % final)