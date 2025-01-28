
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













