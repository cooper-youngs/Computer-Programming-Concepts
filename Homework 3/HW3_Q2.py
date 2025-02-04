"""Please write a Python program which asks the user to enter a list of integers and then prints out the maximum 
value in that list. Keep in mind that generally speaking, you can and should just use the max() function 
but in this problem you should avoid using it."""

L = [x for x in input("Please enter a list of integers:").split()]

#newList = [x for x in L if x > L[i - 1]]
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if j > i:
            max = L[j]

print(max)