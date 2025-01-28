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
        
        
        
        




