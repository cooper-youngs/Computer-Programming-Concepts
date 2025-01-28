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