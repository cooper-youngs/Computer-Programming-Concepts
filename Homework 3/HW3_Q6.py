"""Write a Python program which first reads in a list of integers L and prints out the index i such
that L[i] is as small as possible. If there are multiple such indices, print any of them."""

L = [int(x) for x in input("Please enter a list of integers").split()]
# smol = []
"""
for i, x in enumerate(L):
    if x <= L[i - 1]:
        print(x)
        print(L[i - 1])
        smol.append(x)

print(smol)"""

#for loop that iterates through each element, with access to both index and value
#able to compare current index to that index plus 1
#condition that current element is less than
#i dont understand how sometimes the i or j in these statements would return the actual element and sometimes the index
#see below

"""its because when we do 
for i in L:
this is iterating through each element of the list L & i will take on the value of each element, each iteration.
when you do 
for i in range(len(L)) - the range and len functions return a sequence of indices, and those indices are then iterated on
subsequently the i takes on the value of each index.
"""
"""Seems like i should be able to do this more efficiently, this iterating through the entire j loop 
for eac iteration of the i loop, see problem three and try to implement"""
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if i < j:
            smol = i

print(f"Smallest integer is in index:{smol}")