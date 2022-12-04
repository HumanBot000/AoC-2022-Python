"""
Today I don't upload the input
"""
import re

counter = 0
input = open("aoc-04-input.txt","r")
for i in input.readlines():
    check = True
    numbers_first = []
    numbers_second = []
    first = re.split(",",i)[0]
    second = re.split(",", i)[1]
    first_f_digit = int(re.split("-",first)[0])
    first_s_digit = int(re.split("-", first)[1])
    second_f_digit = int(re.split("-", second)[0])
    second_s_digit = int(re.split("-", second)[1])
    if first_f_digit <= second_f_digit and first_s_digit >= second_s_digit:
        counter = counter + 1
        check = False
    if second_f_digit <= first_f_digit and second_s_digit >= first_s_digit and check:
        counter = counter + 1
print(counter)