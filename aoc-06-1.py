input = open("aoc-06-input.txt","r")
last_four = []
counter = 0
for i in input.read():
    counter = counter + 1
    if len(last_four) == 4:
        last_four.remove(last_four[0])
    last_four.append(i)
    if len(last_four) == 4:
        if not last_four[0] == last_four[1] and not last_four[0] == last_four[2]and not last_four[0] == last_four[3]:
            if not last_four[1] == last_four[0] and not last_four[1] == last_four[2] and not last_four[1] == last_four[3]:
                if not last_four[2] == last_four[1] and not last_four[2] == last_four[0] and not last_four[2] == last_four[3]:
                    if not last_four[3] == last_four[1] and not last_four[3] == last_four[2] and not last_four[3] ==last_four[0]:
                        print(counter)
                        print(last_four)
                        break