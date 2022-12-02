"""
A Rock
B Paper
C Scissors
-----------
X Lose
Y Draw
Z Win
-----------
1 for Rock, 2 for Paper, and 3 for Scissors + 0 if you lost, 3 if the round was a draw, and 6 if you won
"""

input = open("aoc-02-input.txt", "r")
points = 0
for i in input.readlines():
    opponent = i[0]
    end = i[2]  # Because of the Space between the letters
    if end == "X":
        points = points + 0
        if opponent == "A":
            points = points + 3
        elif opponent == "B":
            points = points + 1
        elif opponent == "C":
            points = points + 2
    elif end == "Y":
        points = points + 3
        if opponent == "A":
            points = points + 1
        elif opponent == "B":
            points = points + 2
        elif opponent == "C":
            points = points + 3
    if end == "Z":
        points = points + 6
        if opponent == "A":
            points = points + 2
        elif opponent == "B":
            points = points + 3
        elif opponent == "C":
            points = points + 1
print(points)
