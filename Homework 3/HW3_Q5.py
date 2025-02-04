"""Write a Python program which first reads in a list of integers. Then it does the following things:
(a) Prints out the range of the list. (b) Prints out the median of the list."""


userList = [int(x) for x in input("Please enter a list of integers:").split()]

minNum = min(userList)
maxNum = max(userList)
print(f"Range is :{minNum} - {maxNum}")

#to find median first sort values
userList.sort()

#need to find middle index, do this by adding 1 to the length of the list and dividing by 2
#if it comes out with a remainder the median the number halfway between that index rounded down and that index rounded up
#so if there are 48 numbers, 49/2 = 24.5, the median is halfway between list[24] and list[25] so add them and divide by 2
#need to subract one from indices because we are calculating the nth number, which would be nth - 1 index
if (len(userList) + 1) % 2 == 0:
    medIndex = (len(userList) + 1) // 2
    median = userList[medIndex - 1]
else:
    lowIndex = (len(userList) + 1) // 2
    upperIndex = lowIndex + 1
    lowNum = userList[lowIndex - 1]
    upperNum = userList[upperIndex - 1]
    median = (lowNum + upperNum) / 2

print(f"Median is: {median}")
