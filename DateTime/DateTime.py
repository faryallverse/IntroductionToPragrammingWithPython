#Working with dates and time

#datetime is a library. A library is a collection of precompiled routines and methods for you to use in your program.
#The datetime class allows us to get the current date and time, as well as perform various operations on dates and times.
#The import statement is used to import the datetime module, which contains the datetime class.
import datetime
#The datetime.now() method returns the current date and time as a datetime object.
print(datetime.datetime.now())
#today is a function that returns the current date as a datetime object.
print(datetime.date.today())

currentDate = datetime.datetime.now()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

#Date Formats 
#strftime() allows you to specify the date format
# %b:month abbreviation, %m: month as a zero-padded decimal, %B: full month name, %y: two digit year, %Y: four digit year, %d: day of the month, %a: weekday abbreviated, %A: day of the week (For full list of format codes, see https://strftime.org/))
print(currentDate.strftime('%d %b %y')) # 01 Jan 26
print(currentDate.strftime('%d %B, %Y')) # 01 January, 2026
print(currentDate.strftime('%A, %d %B %Y')) # Wednesday, 01 January 2026
print(currentDate.strftime('Today is %a, %d %b %y.')) # Wed, 01 Jan 26

#What if I want another language? The locale module allows you to set the locale for your program, which affects the way dates and times are formatted. For details, see http://babel.pocoo.org/

birthday = input('What is your birthday? (dd/mm/yyyy): ')
#Right now, birthday is a string. If we want to treat it like a date, we must convert the datatype of the variable birthday into date.
#The strptime() method allows us to convert a string into a datetime object. The first argument is the string to be converted, and the second argument is the format of the string.
dob = datetime.datetime.strptime(birthday, '%d/%m/%Y').date()
#We used datetime twice because the strptime() is a function in the datetime class, which is in the datetime module.
print(dob)
print(dob.year)
print(dob.month)
print(dob.day)
print(dob.strftime('%A, %d %B %Y')) # Wednesday, 01 January 2026
print(dob.strftime('You were born on a %A.')) # You were born on a Wednesday.

#Creating a countdown to my next birthday
nextBirthday = datetime.datetime.strptime('31/12/2026', '%d/%m/%Y').date()
currentDate = datetime.date.today()
#Just subtract the two dates
difference = nextBirthday - currentDate
print('There are %d days until your next birthday.' % difference.days)

#Dealing with time
currentTime = datetime.datetime.now()
print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

#Time Formats
# %H: hour (24-hour clock), %I: hour (12-hour clock), %p: AM/PM, %M: minute, %S: second
print(currentTime.strftime('%H:%M:%S')) # 14:30:00
print(currentTime.strftime('%I:%M:%S %p')) # 02:30:00 PM
