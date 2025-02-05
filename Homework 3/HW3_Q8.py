"""Write a program which first reads in a list of integers L which represents the game results of a soccer team. 
For example L = [1, 1, 1, 0, 1, 0, 0] means that the team won the first 3 games, lost the 4th game, won the 5th game,
 and lost the 6th and 7th game. Print out the longest winning this streak. 
 In this example, the longest winning streak is 3."""

L = [int(x) for x in input("Please enter a list of integers:").split()]

longStreak = 0
currentStreak = 0

for elem in L:
    if elem == 1:
        currentStreak +=1
    else:
        if currentStreak > longStreak:
            longStreak = currentStreak
            currentStreak = 0
        

print(f"Longest winning streak is {longStreak} games.")