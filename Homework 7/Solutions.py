# #1
# """
# Consider an algorithm that takes as input a positive integer n. If n is even, 
# the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. 
# The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
# $$ 3 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$$

# """
# userNum = int(input("Please enter a number"))

# while userNum != 1:
#     if userNum % 2 == 0:
#         userNum /= 2
#     else:
#         userNum *= 3 
#         userNum += 1
#     print(userNum)


# #2
# """
# You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.

# Input
# The first input line contains an integer n.
# The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).

# Output
# Print the missing number.
# """


# countNums = int(input("Please enter how many numbers are in the list: "))
# userNums = [int(x) for x in input("Enter all numbers except for one: ").split()]

# allNums = [x for x in range(1, countNums + 1)]

# for num in userNums:
#     allNums.remove(num)

# print(allNums[0])

# #3
# """
# You are given a DNA sequence: a string consisting of characters A, C, G, and T. 
# Your task is to find the longest repetition in the sequence. This is a maximum-length 
# substring containing only one type of character.A

# Input
# The only input line contains a string of n characters.

# Output
# Print one integer: the length of the longest repetition.
# """

# userSeq = [str(x) for x in input("Please enter a DNA sequence of A,C,G,T's with no spaces: ")]

# count = 1 
# maxCount = 1
# print(userSeq)
# for i in range(len(userSeq) - 1):
#     if userSeq[i] == userSeq[i + 1]:
#         count += 1
#         if count > maxCount:
#             maxCount = count
#     else:
#         count = 1
# print(maxCount)


# #4
# """
# You are given an array of n integers. You want to modify the array so that it is increasing, 
# i.e., every element is at least as large as the previous element.

# On each move, you may increase the value of any element by one. 
# What is the minimum number of moves required?

# Input
# The first input line contains an integer n: the size of the array.
# Then, the second line contains n integers x_1,x_2,\ldots,x_n: the contents of the array.

# Output
# Print the minimum number of moves.
# """

# countNums = int(input("Please enter the count of numbers in list: "))
# userSeq = [int(x) for x in input("Enter the numbers in the array in any order: ").split()]

# moves = 0

# for i in range(1 ,countNums):
#     while userSeq[i] < userSeq[ i - 1]:
#         userSeq[i] += 1
#         moves += 1
# print(moves)

# #5
# """
# A permutation of integers 1,2,\ldots,n is called beautiful if there are no adjacent elements whose 
# difference is 1.
# Given n, construct a beautiful permutation if such a permutation exists.

# Input
# The only input line contains an integer n.

# Output
# Print a beautiful permutation of integers 1,2,\ldots,n. If there are several solutions, 
# you may print any of them. If there are no solutions, print "NO SOLUTION".
# """

# maxNum = int(input("Please enter the count of numbers you want starting from zero: "))
# possibleNums = [int(x) for x in range(1, maxNum)]
# beautifulList = []

# if maxNum == 1:
#     print(1)
# elif maxNum == 2:
#     print("NO SOLUTION")
# else:
#     for i in range(len(possibleNums)):
#         if possibleNums[i] % 2 == 0:
#             beautifulList.append(possibleNums[i])
#     for i in range(len(possibleNums)):
#         if possibleNums[i] % 2 != 0:
#             beautifulList.append(possibleNums[i])

# if len(beautifulList) == len(possibleNums):
#     print(beautifulList)
# else:
#     print("NO SOLUTION")

# 6
# """
# You are given a list of n integers, and your task is to calculate the number of distinct values in the list.

# Input
# The first input line has an integer n: the number of values.
# The second line has n integers x_1,x_2,\dots,x_n.

# Output
# Print one integers: the number of distinct values.
# """

# countNums = int(input("Please enter how many numbers are in the list: "))
# userNums = [int(x) for x in input("Enter all numbers: ").split()]

# distinctNums =[]


# distinctNums.append(userNums[0])

# for i in range(1, countNums):
#     if userNums[i] not in distinctNums:
#         distinctNums.append(userNums[i])

# print(len(distinctNums))


# 7
# """
# You are given an array of n integers, and your task is to find two values (at distinct positions) 
# whose sum is x.

# Input
# The first input line has two integers n and x: the array size and the target sum.
# The second line has n integers a_1,a_2,\dots,a_n: the array values.

# Output
# Print two integers: the positions of the values. If there are several solutions, you may print any of them. 
# If there are no solutions, print IMPOSSIBLE.
# """

# userNums = [ int(x) for x in input("Please enter the array size and target sum: ").split()]
# arrayVals = [int(x) for x in input("Please enter the array values: ").split()]

# foundSolution = False
# solutionIndexes = []
# for i in range(len(arrayVals)):
#     if foundSolution == False:
#         for j in range(len(arrayVals)):
#             if arrayVals[i] + arrayVals[j] == userNums[1] and i != j:
#                 solutionIndexes.append(i + 1)
#                 solutionIndexes.append(j + 1)
#                 foundSolution = True
#                 break

# if foundSolution == True:
#     print(solutionIndexes[0], solutionIndexes[1])
# else:
#     print("IMPOSSIBLE")


# #8
# """
#  Please write a Python program which asks the user to input some number of miles and prints out how
#  many kilometers that is. Please use the conversion: 1 mile = 1.60934 kilometers.
# """

# miles = float(input("Pleae enter the number of miles to convert to Kilometers (Either as a whole or decimal number): "))

# print(f"That is {miles * 1.60934} in Kilometers")

# #9
# """
#  Please write a Python program which calculates and prints the value of
#  3 ×(7−2)+1.1
# """

# number = 3 * (7 - 2) + 1.1

# print(number)

# #10
"""
Please write a Python program which prints a diamond like the one below. For 1 additional extra credit
 point, instead write a Python program which asks the user for the number of rows and prints the diamond
 shape below with that many rows. For example, the diamond below has 7 rows.
 7 x 7 diamond
"""

for i in range(7 // 2):
    spaces = " " * ((7 // 2) - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

stars = '*' * (2 * (7// 2) + 1)
print(stars)

for i in range((7 // 2) - 1, -1, -1):
    spaces = ' ' * (7 // 2 - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)
   