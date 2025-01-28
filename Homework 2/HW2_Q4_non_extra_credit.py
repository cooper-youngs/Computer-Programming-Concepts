"""Please write a Python program which asks the user for an integer x (1 ≤ x ≤ 108) and prints how
many integers from 1 to x inclusive are divisible by either 2 or 3. For extra credit, come up with
an O(1) solution to this problem."""

#get user input
userInt = int(input("Please enter a positive integer:"))

#initialize counts at 0
divByTwo = 0
divByThree = 0
divByBoth = 0


#previously had elifs for i % 3 and i % 2 and i % 3, dont want this because elif will only execute if the original if evaluates to False
#since one number could be divisible by both 2 and 3 we dont want the first if statement to evaluate to true and not execute the other two statements
for i in range(1, userInt + 1):
    if i % 2 == 0:
        divByTwo += 1
    if i % 3 == 0:
        divByThree += 1
    if i % 2 == 0 and i % 3 == 0:
        divByBoth += 1
        
total = divByTwo + divByThree - divByBoth

print(f"{total}")
        
        
        
        




