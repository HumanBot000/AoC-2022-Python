"""
Today I don't upload the input
"""
import re

counter = 0
input = open("aoc-04-input.txt", "r")
for i in input.readlines():
    check = False
    numbers_first = []
    numbers_second = []
    first = re.split(",", i)[0]
    second = re.split(",", i)[1]
    first_f_digit = int(re.split("-", first)[0])
    first_s_digit = int(re.split("-", first)[1])
    second_f_digit = int(re.split("-", second)[0])
    second_s_digit = int(re.split("-", second)[1])
    for j in range(first_f_digit, first_s_digit + 1):
        numbers_first.append(j)
    for j in range(second_f_digit, second_s_digit + 1):
        numbers_second.append(j)
    for number in numbers_first:
        if number in numbers_second:
            check = True
            counter = counter + 1
            break
    if check == False:
        for number in numbers_second:
            if number in numbers_first:
                check = True
                counter = counter + 1
                break
print(counter)