
def formatDate(d1, d2):
    import datetime
    issuanceDate = d1.strftime('%d-%B-%Y, %A')
    expiryDate = d2.strftime('%d-%B-%Y, %A')
    message = 'Your CNIC is valid from ' + issuanceDate + ' to ' + expiryDate + '.'
    return message

import datetime
d1 = input('Enter the issuance date of your CNIC(dd/mm/yyyy): ')
d2 = input('Enter the expiry date of your CNIC(dd/mm/yyyy): ')
issuance = datetime.datetime.strptime(d1, '%d/%m/%Y')
expiry = datetime.datetime.strptime(d2, '%d/%m/%Y')

print (formatDate(issuance, expiry))
