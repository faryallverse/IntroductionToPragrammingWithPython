import datetime
userDeadline = input('Enter the deadline of your project (dd/mm/yyyy): ')
deadline = datetime.datetime.strptime(userDeadline, '%d/%m/%Y').date()
currentDate = datetime.date.today()
difference = deadline - currentDate

print('There are %d days until your project deadline.' % difference.days)

weeks = difference.days // 7
days = difference.days % 7

print('That is %d weeks and %d days.' % (weeks, days))