"""
Groups by three
"""
import string

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
line = 0
points = 0
found = False
input = open("aoc-03-input.txt", "r")
lines = input.readlines()
for i in range(0,299,3):
    first = lines[i]
    second = lines[i+1]
    third = lines[i+2]
    for j in lower_case:
        if j in first and j in second and j in third:
            points = points + lower_case.find(j) + 1
            found = True
            break
    if not found:
        for k in upper_case:
            if k in first and k in second and k in third:
                points = points + upper_case.find(k) + 27
                break
    found = False
print(points)

#Today I learned that it is posible to use steps at range()