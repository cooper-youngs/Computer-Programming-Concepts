"""Please write a Python program which reads in a list of integers and prints out how many of the integers are even.
 Here’s an example input and output:
Input: 1 3 2 4 5
Output: 2
Please note that you can read in a list of integers L with the code
L = list(map(int, input().split())) or L = [int(x) for x in input().split()]********
Please memorize one of these ways of writing code for future quizzes/exams and note that whenever I 
ask you to read in a list as an input, I intend on you reading it through the above input format (unless otherwise specified)."""

L = [int(x) for x in input().split()]
count = 0


for i in L:
    if i % 2 == 0:
        count += 1

print(count)
