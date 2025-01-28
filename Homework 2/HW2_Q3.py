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





