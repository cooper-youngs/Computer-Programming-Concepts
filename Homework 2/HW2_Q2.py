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