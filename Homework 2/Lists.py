"""List are data structures that can hold other data types. 
"""

L = [1, 2, 3, 4]

#printing a list and showing that it has its own class, when printing like this it prints with []
print(L)
print(type(L))

#series is the sum of a sequence
# sequence 1, 2, 3, 4, 5
# series 1, 2, 3, 6, 12???

#accessing elements of a list; index starts at 0 so accessing the 3rd index returns the 4th number
print(L[3])

#lists can hold multiple data types
L = [1, 2, 3, 'cat']

#can initialize empty list 
P = []

#can use .append to add an element to the end of the list
P.append(1)
print(P)
P.append(2)

#adding an element to the end is not hard because all of the indexes stay
#the same for all of the other elements, just need to extend the size of the
#list

#to add an element to the beginning of a list all elements must first be 
# shifted to the right index wise, then insert at the Oth index

#can get around this with queues, also have double ended queue's to get 
#efficient insertion at the beginning or end.

#read in list from user write a computer program to go through a list and print out how many positive integers are in it.
#numbers have to type int and seperated by a space
#memorize this code
#.split() separates the numbers, by default separates by spaces
#basically saying for each x in input, split by space, typecase to type int

#for "element" in "list", return element as an integer and append to this new list
x = [int(x) for x in input("Enter a list:").split()]
print(x)


count = 0
for i in x:
    if i > 0:
        count += 1

print(count)

#using list comprehension
x = [int(x) for x in input("Enter a list:").split()]
print(x)


#can use list comprehension to create a new list of all the integers that are positive, then return the length of the list
y = [i for i in x if i > 0]
print(len(y))

#using list comprehension to create a list of booleans, which equates to 1 or 0, then can sum all the elements in the list
print(sum(elem > 0 for elem in x))


L = [2, 3, 4]


#classic way of iterating through a list, printing each element
for i in range(len(L)):
    print(L[i])

#the way i first did it 
for i in L:
    print(i)

