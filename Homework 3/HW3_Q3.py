"""The dot product of two vectors a and b is given by Pni a ib i. Note that we can simply represent a vector as a list. 
Write a computer program which reads in a list of two integers (each list input is given on a separate line). 
If the lengths of the two lists are different, print IMPOSSIBLE. Otherwise, print out the correct dot product. 
Note that if you would like guidance on this problem, you should come to my office hours.
It might seem hard since it uses linear algebra but it’s actually a quite easy problem. 
Note also that you can use the len() function to check that the lengths of the list are the same initially."""

listOne = [int(x) for x in input("Please enter a list of integers:").split()]
listTwo = [int(x) for x in input("Please enter another list of integers:").split()]
dotProduct = 0

print(listOne)
print(listTwo)

if len(listOne) != len(listTwo):
    print("IMPOSSIBLE.")

else:
    prods = [listOne[i] * listTwo[i] for i in range(len(listOne))]
    print(sum(prods))

# """else:
# This is iterating wrong, its accessing the first elem in listOne then iterating through all of the numbers in listTwo
# before it iterates to the next number in listOne
#     for val in listOne:
#         for valTwo in listTwo:
#             print(val)
#             print(valTwo)
#             dotProduct = dotProduct + (val * valTwo)

#     #dotProduct = [ x * y for x in listOne for y in listTwo]
# print(dotProduct)"""

#Dont need to use a second for loop, since we are comparing elements in different lists but the same index
#can be used to refer to elements in either list


# ans = 0 
# for i in range(len(listOne)):
#     ans += listOne[i] * listTwo[i]

# ans = 0
# for val1, val2 in zip(listOne, listTwo):
#     ans += val1 * val2 



