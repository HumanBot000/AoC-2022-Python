"""
A Rock
B Paper
C Scissors
-----------
X Rock
Y Paper
Z Scissors
-----------
1 for Rock, 2 for Paper, and 3 for Scissors + 0 if you lost, 3 if the round was a draw, and 6 if you won
-----------
A Y - Rock-Paper
B X - Paper-Rock
C Z - Scissors-Scissors
-----------
What would your total score be if everything goes exactly according to your strategy guide?
"""

input = open("aoc-02-input.txt", "r")
points = 0
for i in input.readlines():
    opponent = i[0]
    me = i[2]  # Because of the Space between the letters
    if me == "X":  # Rock
        points = points + 1
        if opponent == "A":
            points = points + 3
        elif opponent == "B":
            points = points + 0
        elif opponent == "C":
            points = points + 6
    elif me == "Y":  # Paper
        points = points + 2
        if opponent == "A":
            points = points + 6
        elif opponent == "B":
            points = points + 3
        elif opponent == "C":
            points = points + 0
    elif me == "Z":  # Scissors
        points = points + 3
        if opponent == "A":
            points = points + 0
        elif opponent == "B":
            points = points + 6
        elif opponent == "C":
            points = points + 3
print(points)
