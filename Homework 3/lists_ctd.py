
#diff ways to loop through a list

n = len(L)
for i in range(n):
    print(L[i])


for elem in L:
    print(elem)

#this will 
for index, elem in enumerate(L):
    print(index, elem)


#to compare two lists, comparing elements of the same index

for i in range(len(L)):
    if L[i] == B[i]:
        print(L[i])