input = open("aoc-01-input.txt","r")
most_1 = 0
most_2 = 0
most_3 = 0
currently = 0
for i in input.readlines():
    if i == "\n":
        if currently > most_1:
            most_1 = currently
        elif currently > most_2:
            most_2 = currently
        elif currently > most_3:
            most_3 = currently
        currently = 0
    else:
        currently = currently + int(i)
print(int(most_1)+int(most_2)+int(most_3))