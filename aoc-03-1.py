"""
2 compartments
--------------
split things in middle
--------------
find doubles
--------------
Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
"""
import string

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
points = 0
input = open("aoc-03-input.txt", "r")
for i in input.readlines():
    first = i[0:int(len(i) / 2)]
    second = i[int(len(i) / 2):len(i)]
    for j in second:
        if j in first:
            if j in lower_case:
                points = points + 1 + lower_case.find(j)
            else:
                points = points + 27 + upper_case.find(j)
            break
print(points)

