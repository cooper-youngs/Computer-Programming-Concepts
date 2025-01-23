"""Please write a Python program which asks the user to input some number of miles and prints out
 how many kilometers that is. Please use the conversion: 1 mile = 1.60934 kilometers."""

miles = 0
miles = float(input("Please enter a number of miles to convert to kilometers: "))
kilometers = miles * 1.60934
answer = print(f"{miles} miles is {kilometers} kilometers")
    







"""Please write a Python program which calculates and prints the value of  3 x (7 - 2) + 1.1"""
value = 3 * (7 - 2) + 1.1
print(value)




""" Please write a Python program which prints a diamond like the one below. For 1 additional extra
 credit point, instead write a Python program which asks the user for the number of rows and prints
 the diamond shape below with that many rows. For example, the diamond below has 7 rows."""



rows = int(input("Enter the number of rows you want in the diamond: "))

#upper half of diamond loop
for i in range(rows // 2):
    spaces = ' ' * (rows // 2 - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

#middle row for odd number of rows
if rows % 2 != 0:
    #spaces = ' ' * (rows // 2)
    stars = '*' * (2 * (rows// 2) + 1)
    print(stars)

#lower half of diamond loop
for i in range(rows // 2 - 1, -1, -1):
    spaces = ' ' * (rows // 2 - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)




"""Please write a Python program which asks for your annual salary and what percent of that salary
 you are paying for taxes. Finally print your after tax income."""

salary = float(input("Please enter your salary: "))
taxPercentage = float(input("Please enter what percentage of your salary you are paying for taxes (please omit the %): "))
if taxPercentage < 1: 
   netIncome = salary * (1 - taxPercentage)
   print(f"Your after tax income is: {netIncome}" )
else:
    taxPercentageAdjusted = taxPercentage/100
    netIncome = salary * (1 - taxPercentageAdjusted)
    print(f"Your after tax income is: {netIncome}" )

"""Please write a Python program which asks the user for the distance to a city (in miles) they need
 to drive to, asks at what average speed they can drive at (in miles per hour), and prints out how
 much time it will take them."""

miles = int(input("Please enter the distance (in miles) you need to drive: "))
speed = int(input("At what average speed (in MPH) are you able to drive to this location: "))
time = miles / speed
print(f"It will take you approximately {time} hours to reach your destination.")






"""Please write a Python program which asks the user on what year they were born and prints their
 current age (you can approximate I know the specific day you are born on matters).
 For 1 additional extra credit point, alternatively ask the user what exact day, month, and year
 they were born at and print out their age based on the time the Python program is being run at.
 Hint: The datetime library may be helpful"""

from datetime import datetime

birthDate = str(input("Please enter your birthdate in mm/dd/yyyy format: "))
formattedDate = datetime.strptime(birthDate, "%m/%d/%Y")
print(formattedDate)

birthMonth = formattedDate.month
birthDay = formattedDate.day
birthYear = formattedDate.year


todayDate = datetime.today()
todayMonth = todayDate.month
todayDay = todayDate.day
todayYear = todayDate.year

if todayMonth <= birthMonth:
    if todayDay >= birthDay:
        age = todayYear - birthYear
    else:
        age = todayYear - birthYear - 1
else:
    age = todayYear - birthYear

print(age)


