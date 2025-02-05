"""Write a program which first reads in a list of integers L and prints out YES if there exist indices
i ̸= j such that L[i] + L[j] = 0 and otherwise prints NO."""

L = [int(x) for x in input("Please input a list of integers:").split()]

#print yes if there exists two numbers thats sum is 0
#print 0 if any two numbers are opposite

isOpp = "NO"

for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if L[i] + L[j] == 0:
            isOpp = "YES"
            
print(f"{isOpp}")

