"""Please write a Python program which asks the user to enter a list of integers and then prints out the maximum 
value in that list. Keep in mind that generally speaking, you can and should just use the max() function 
but in this problem you should avoid using it."""

L = [int(x) for x in input("Please enter a list of integers:").split()]

#newList = [x for x in L if x > L[i - 1]]
#this works, but it compares each number to every other number in the list, so if the list
#is 4 numbers long, it must iterate 12 times (3 combinations per number)
#should just iterate through once and keep track of the current biggest number
## REDO REDO REDO REDO REDO REDO
"""for i in range(len(L)):
    for j in range(i + 1, len(L)):
        print(L[i])
        print(L[j])
        if j > i:
            max = L[j]
"""

#best solution
max = 0
for i in range(len(L)):
    if L[i] > max:
        max = L[i]

print(max)

#[1,2,4,7]
#1,2 1,4 1,7
#2,1 2,4 2,7
#4,1 4,2 4,7
#7,1 7,2 7,4