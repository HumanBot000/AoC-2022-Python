input = open("aoc-01-input.txt","r")
most = 0
currently = 0
for i in input.readlines():
    if i == "\n":
        if currently > most:
            most = currently
        currently = 0
    else:
        currently = currently + int(i)
print(most)