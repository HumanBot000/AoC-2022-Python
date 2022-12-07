input = open("aoc-06-input.txt","r")
last_four_teen = []
counter = 0
for i in input.read():
    counter = counter + 1
    if len(last_four_teen) == 14:
        last_four_teen.remove(last_four_teen[0])
    last_four_teen.append(i)
    myset = set(last_four_teen)
    if len(myset) == 14:
        print(counter)
        break
