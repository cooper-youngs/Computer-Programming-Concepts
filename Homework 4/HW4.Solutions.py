"""
Please write the code for the following problems from Chapter 13 of this book:
 1, 2, 4, 5, 6, 9, 12, 14, 16, 20, 21, 23. 
 


 """

"""
Write a function called rectangle that takes two integers m and n as arguments and prints
 out an m×n box consisting of asterisks. Shown below is the output of rectangle(2,4)
 """

def rectangle(m: int, n: int):
    for i in range(m):
        print("*" * n)

rectangle(2,4)

"""
 2. 
 (a) Write a function called add_excitement that takes a list of strings and adds an excla
mation point (!) to the end of each string in the list. The program should modify the
 original list and not return anything.
 
 (b) Write the same function except that it should not modify the original list and should
 instead return a new list.
 """
stringList = ["hi", "there", "bud"]
def add_excitement(stringList: list): 
    for i in range(len(stringList)):
        stringList[i] += "!"

    

def add_excitement(stringList: list): 
    newList = []
    for i in range(len(stringList)):
        newList.append(stringList[i] + "!")

add_excitement(stringList)

"""
4. 
The digital root of a number n is obtained as follows: Add up the digits n to get a new number.
 Add up the digits of that to get another new number. Keep doing this until you get a number
 that has only one digit. That number is the digital root.
 For example, if n = 45893, we add up the digits to get 4+5+8+9+3=29. We then add up
 the digits of 29 to get 2+9 = 11. We then add up the digits of 11 to get 1+1 = 2. Since 2 has
 only one digit, 2 is our digital root.
 
 """

num = 45893


def digitalRoot(num: int):
    
    numAsString = str(num)

    while len(numAsString) > 1:
        currentSum = 0

        for i in range(len(numAsString)):
            currentSum += int(numAsString[i])

        numAsString = str(currentSum)

    numAsString = int(numAsString)

    return print(numAsString)


digitalRoot(num)

"""
5.
 Write a function called first_diff that is given two strings and returns the first location in
 which the strings differ. If the strings are identical, it should return-1.
"""

def first_diff(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    minLen = min(len1, len2)

    for i in range(minLen):
        if str1[i] != str2[i]:
            return i
    
    if len1 == len2:
        return -1
    else:

        return minLen

str1 = "Jacobs"
str2 = "Jacob"

print(first_diff(str1, str2))


"""
6. Write a function called binom that takes two integers n and k and returns the binomial coefficient n k.
 .
"""

def coeff(n , k):
    biCoeff = abs(n) / (abs(k) * abs((n - k)))

    return biCoeff

print(coeff(1, 9))

"""
9. Write a function called factors that takes an integer and returns a list of its factors.

"""

def factors(n):

    loop = n // 2 + 1
    facList = []

    for i in range(1, loop):
        if n % i == 0:
            facList.append(i)

    return facList

print(factors(20))

"""
12. Recall that if s is a string, then s.find('a') will find the location of the first a in s. The
 problem is that it does not find the location of every a. Write a function called findall that
 given a string and a single character, returns a list containing all of the locations of that 
 character in the strin

"""
str = "Vikings" 
char = "i"
def findAll(str, searchChar):
    locs = []

    for i in range(len(str)):
        if str[i] == searchChar:
            locs.append(i)
            
    return locs

print(findAll(str, char))


"""
14. Write a function called is_sorted that is given a list and returns True if the list is sorted
 and False otherwise.
 
 """

def is_sorted(L):

    for i in range(len(L)- 1):
        if L[i] > L[i + 1]:
            return False
        
    return True
    
L = "12432"

print(is_sorted(L))


"""
16. Write a function called one_away that takes two strings and returns True if the strings are of
 the same length and differ in exactly one letter, like bike/hike or water/wafer.
 """

def one_away(str1, str2):

    count = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1

    if (len(str1) == len(str2)) and count == 1:
        return True
    
    return False

print(one_away("Vikes", "Vikeds"))


"""
20. Write a function called merge that takes two already sorted lists of possibly different lengths,
 and merges them into a single sorted list.
 (a) Do this using the sort method.
 (b) Do this without using the sort method.
 
 """

def merge(L1, L2):
    newList = []
    maxLen = max(len(L1), len(L2))

    newList = L1 + L2
    newList.sort()

    return newList


L1 = [1, 2, 3, 4, 5]
L2 = [4, 5, 6, 7]

# print(merge(L1, L2))

def merge(L1, L2):
    newList = []
    i = 0 
    j = 0

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            newList.append(L1[i])
            i += 1
        else:
            newList.append(L2[j])
            j += 1

    while i < len(L1):
        newList.append(L1[i])
        i += 1
    
    while j < len(L2):
        newList.append(L2[j])
        j += 1
    
    return newList

print(merge(L1, L2))


"""
21. In Chapter 12, the way we checked to see if a word w was a real word was:
 if w in words:
 where wordswasthelist of words generated from a wordlist. This is unfortunately slow, but
 there is a faster way, called a binary search. To implement a binary search in a function, start
 by comparing w with the middle entry in words. If they are equal, then you are done and
 the function should return True. On the other hand, if w comes before the middle entry, then
 search the first half of the list. If it comes after the middle entry, then search the second half of
 the list. Then repeat the process on the appropriate half of the list and continue until the word
 is found or there is nothing left to search, in which case the function short return False. The
 < and>operators can be used to alphabetically compare two strings.
 """

def binary_search(words, w):
    words.sort()
    left = 0
    right = len(words) - 1

    while left <= right:

        mid = (left + right) // 2
    
    
        if words[mid] == w:
            return True 
        elif w < words[mid]:
            right = mid - 1  
        else:
            left = mid + 1  

    return False 


words = ["vikes", "score", "touchdown"]
w = "vikes"

print(binary_search(words,w))

"""
23. Write a function that is given a 9 × 9 potentially solved Sudoku and returns True if it is
 solved correctly and False if there is a mistake. The Sudoku is correctly solved if there are
 no repeated numbers in any row or any column or in any of the nine “blocks.”

"""

def is_valid_sudoku(sudoku):
    # Check rows
    for row in sudoku:
        if not is_unique(row):
            return False

    for col in range(9):
        column = [sudoku[row][col] for row in range(9)]
        if not is_unique(column):
            return False

    
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            block = []
            for i in range(block_row, block_row + 3):
                for j in range(block_col, block_col + 3):
                    block.append(sudoku[i][j])
            if not is_unique(block):
                return False

    return True  


def is_unique(section):
    unique_list = []  
    for num in section:
        if num != 0 and num in unique_list:  
            return False  
        unique_list.append(num)  
    return True


sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

print(is_valid_sudoku(sudoku))



        





