"""Please write a Python program which asks the user the distance to their favorite city. Next, the
user is asked at what average speed they are willing to drive at. Finally the program asks the user
how much time they have to reach their favorite city. If there is enough time to reach the user’s
favorite city assuming the user starts driving instantaneously, print ”Enough Time”. Otherwise,
print ”You’re going to be late”.
"""


#prompt user for distance to favorite city
favCityDistance = float(input("Please enter the distance to your favorite city (in miles):"))

#prompt user for average speed
avgSpeed = float(input("Please enter the average speed you are able to drive to your favorite city (in mph):"))

#prompt user for how much time they have to reach destination
timeAvailable = float(input("Please enter the amount of time you have to reach your destination (in minutes):"))

#convert minutes to hours
availableTimeHrs = timeAvailable / 60

#find necessary avg speed
neededSpeed = favCityDistance / availableTimeHrs

#check comparison
print(f"Your speed {avgSpeed}")
print(f"Needed Speed {neededSpeed}")

#if else to compare with avgSpeed
if avgSpeed >= neededSpeed:
    print("Enough Time")
else:
    print("You're going to be late")


"""Please write a Python program which asks the user for a positive integer and prints out the number
of positive factors of that integer. If the user enters 6, the positive factors of 6 are [1, 2, 3, 6]
so the program should print out 4 in this case."""

#get postive integer input, initialize count of factors at 0
inputInteger = int(input("Please enter a positive integer:"))
numFactors = 0

for i in range(1, inputInteger + 1):
    if inputInteger % i == 0: 
        numFactors += 1
        
print(f"{numFactors}")


"""Ask the user how much money they need for retirement. Ask the user how much money they will
add to their bank account every year. Ask the user what rate of growth they expect. Print how
long it will take them to retire. For example, if the rate of growth is 3% and the user puts in $1000
into the account every year, then we can say the following: At the end of year 1, they’ll have
$1000.
At the end of year 2, they’ll have
$(1000 × 1.03 + 1000) = $2030.
At the end of year 3, they’ll have
$(1000 × (1.03)2 + 1000 × 1.03 + 1000) = $3090.90.
"""

#get money needed for retirement
neededMoney = float(input("Please enter the amount of money needed for retirement (in dollars and cents): $"))

#get money added to bank per year
addedMoney = float(input("Please enter the amount of money you'll be able to add to your bank account each year. (in dollars and cents): $"))

#establish rate of growth
growthRate = .03

#initialize principal and year
principal = addedMoney
years = 1

while principal < neededMoney:
    principal = (principal * (1 + growthRate)) + addedMoney
    years += 1

print(f"It will take {years} years for you to retire.")


"""Please write a Python program which asks the user for an integer x (1 ≤ x ≤ 108) and prints how
many integers from 1 to x inclusive are divisible by either 2 or 3. For extra credit, come up with
an O(1) solution to this problem."""

#get user input
userInt = int(input("Please enter a positive integer:"))

#use integer division to find the number of numbers that are divisible by that integer (being divisible by 2 or 3 means being divisible by both)
divByTwo = userInt // 2
divByThree = userInt // 3
divByBoth = userInt // 6



        
total = divByTwo + divByThree - divByBoth

print(f"{total}")


"""Ask the user to enter a temperature in Celsius. The program should 
print a message based on the temperature (Source: A Practical Introduction
 to Python Programming): 
 
 • If the temperature is less than −273.15, print that the temperature is 
 invalid because it is below absolute zero. 
 
 • If it is exactly −273.15, print that the temperature is absolute 0. 
 
 • If the temperature is between −273.15 and 0,
print that the temperature is below freezing. 

• If it is 0, print that the temperature is at the freezing point. 

• If it is between 0 and 100, print that the temperature is in the 
normal range. 

• If it is 100, print that the temperature is at the boiling point. 

• If it is above 100, print that the temperature is above the 
boiling point."""


#Get user input, convert to float. Using cutoffs in decimals
degCelsius = float(input("Please enter the temperature in Celsius:"))


#set intervals for print messages
if degCelsius > 100:
    print("The temperature is above boilpoint point.")
elif degCelsius == 100:
    print("The temperature is at boilpoint point.")

#using 100 > degCelsius > 0 works in python but could also just use and keyword
elif 100 > degCelsius > 0:
    print("The temperature is in the normal range.")

elif degCelsius == 0:
    print("The temperature is at freezing point.")

elif 0 > degCelsius > -273.15:
    print("The temperature is below freezing.")

elif degCelsius == -273.15:
    print("The temperature is absolute zero.")

#as long as all the above conditions are set correctly dont have to set a elif cutoff here it should always 
#execute for any number below -273.15
else:
    print("The temperature is invalid because it is below absolute zero.")

"""Ask the user to enter an integer x (1 ≤ x ≤ 1014).
 Print YES if x is a perfect square, otherwise print NO.
Note: If your program is too slow you’ll only get half credit for this problem."""


userInput = int(input("Please enter a positive integer:"))

#calculate square root by exponentiating to the 1/2 power
sqrtInput = userInput ** .5

#check if perfect square by checking if sqrtInput is an integer
#can do this by dividing by one and making sure the remainder is 0 (x % 1 == 0)
if sqrtInput % 1 == 0:
    print("YES")
else:
    print("NO")