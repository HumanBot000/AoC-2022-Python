stack_one = []
stack_two = []
stack_three = []
stack_four = []
stack_five = []
stack_six = []
stack_seven = []
stack_eight = []
stack_nine = []
input = open("aoc-05-input.txt", "r").readlines()

for line in input[0:8]:
    stack_one.append(line[1])
    stack_eight.append(line[29])
    stack_two.append(line[5])
    stack_three.append(line[9])
    stack_four.append(line[13])
    stack_five.append(line[17])
    stack_six.append(line[21])
    stack_seven.append(line[25])
    stack_nine.append(line[33])
stack_one = [ele for ele in stack_one if ele.strip()]
stack_two = [ele for ele in stack_two if ele.strip()]
stack_three = [ele for ele in stack_three if ele.strip()]
stack_four = [ele for ele in stack_four if ele.strip()]
stack_five = [ele for ele in stack_five if ele.strip()]
stack_six = [ele for ele in stack_six if ele.strip()]
stack_seven = [ele for ele in stack_seven if ele.strip()]
stack_eight = [ele for ele in stack_eight if ele.strip()]
stack_nine = [ele for ele in stack_nine if ele.strip()]
for i in input[10::]:  # To end
    amount = int(i[5])
    try:
       _from = int(i[12])
    except:
        _from = int(i[13])
    try:
        to = int(i[17])
    except:
        to = int(i[18])
    for j in range(1,amount):
        if _from == 3 :
            temp = stack_three[0]
            stack_three.remove(stack_three[0])
            if to == 1:
                stack_one[0:0] = [temp]
            elif to == 2:
                stack_two[0:0] = [temp]
            elif to == 3:
                stack_three[0:0] = [temp]
            elif to == 4:
                stack_four[0:0] = [temp]
            elif to == 5:
                stack_five[0:0] = [temp]
            elif to == 6:
                stack_six[0:0] = [temp]
            elif to == 7:
                stack_seven[0:0] = [temp]
            elif to == 8:
                stack_eight[0:0] = [temp]
            elif to == 9:
                stack_nine[0:0] = [temp]
        elif _from == 2:
            temp = stack_two[0]
            stack_two.remove(stack_two[0])
            if to == 1:
                stack_one[0:0] = [temp]
            elif to == 2:
                stack_two[0:0] = [temp]
            elif to == 3:
                stack_three[0:0] = [temp]
            elif to == 4:
                stack_four[0:0] = [temp]
            elif to == 5:
                stack_five[0:0] = [temp]
            elif to == 6:
                stack_six[0:0] = [temp]
            elif to == 7:
                stack_seven[0:0] = [temp]
            elif to == 8:
                stack_eight[0:0] = [temp]
            elif to == 9:
                stack_nine[0:0] = [temp]
        elif _from == 1:
            try:
                temp = stack_one[0]
            except:
                pass

            stack_one.remove(stack_one[0])
            if to == 1:
                stack_one[0:0] = [temp]
            elif to == 2:
                stack_two[0:0] = [temp]
            elif to == 3:
                stack_three[0:0] = [temp]
            elif to == 4:
                stack_four[0:0] = [temp]
            elif to == 5:
                stack_five[0:0] = [temp]
            elif to == 6:
                stack_six[0:0] = [temp]
            elif to == 7:
                stack_seven[0:0] = [temp]
            elif to == 8:
                stack_eight[0:0] = [temp]
            elif to == 9:
                stack_nine[0:0] = [temp]
        elif _from == 4:
            temp = stack_four[0]
            stack_four.remove(stack_four[0])
            if to == 1:
                stack_one[0:0] = [temp]
            elif to == 2:
                stack_two[0:0] = [temp]
            elif to == 3:
                stack_three[0:0] = [temp]
            elif to == 4:
                stack_four[0:0] = [temp]
            elif to == 5:
                stack_five[0:0] = [temp]
            elif to == 6:
                stack_six[0:0] = [temp]
            elif to == 7:
                stack_seven[0:0] = [temp]
            elif to == 8:
                stack_eight[0:0] = [temp]
            elif to == 9:
                stack_nine[0:0] = [temp]
        elif _from == 5:
            temp = stack_five[0]
            stack_five.remove(stack_five[0])
            if to == 1:
                stack_one[0:0] = [temp]
            elif to == 2:
                stack_two[0:0] = [temp]
            elif to == 3:
                stack_three[0:0] = [temp]
            elif to == 4:
                stack_four[0:0] = [temp]
            elif to == 5:
                stack_five[0:0] = [temp]
            elif to == 6:
                stack_six[0:0] = [temp]
            elif to == 7:
                stack_seven[0:0] = [temp]
            elif to == 8:
                stack_eight[0:0] = [temp]
            elif to == 9:
                stack_nine[0:0] = [temp]
        elif _from == 6:
            temp = stack_six[0]
            stack_six.remove(stack_six[0])
            if to == 1:
                stack_one[0:0] = [temp]
            elif to == 2:
                stack_two[0:0] = [temp]
            elif to == 3:
                stack_three[0:0] = [temp]
            elif to == 4:
                stack_four[0:0] = [temp]
            elif to == 5:
                stack_five[0:0] = [temp]
            elif to == 6:
                stack_six[0:0] = [temp]
            elif to == 7:
                stack_seven[0:0] = [temp]
            elif to == 8:
                stack_eight[0:0] = [temp]
            elif to == 9:
                stack_nine[0:0] = [temp]
        elif _from == 7:
            temp = stack_seven[0]
            stack_seven.remove(stack_seven[0])
            if to == 1:
                stack_one[0:0] = [temp]
            elif to == 2:
                stack_two[0:0] = [temp]
            elif to == 3:
                stack_three[0:0] = [temp]
            elif to == 4:
                stack_four[0:0] = [temp]
            elif to == 5:
                stack_five[0:0] = [temp]
            elif to == 6:
                stack_six[0:0] = [temp]
            elif to == 7:
                stack_seven[0:0] = [temp]
            elif to == 8:
                stack_eight[0:0] = [temp]
            elif to == 9:
                stack_nine[0:0] = [temp]
        elif _from == 8:
            temp = stack_eight[0]
            stack_eight.remove(stack_eight[0])
            if to == 1:
                stack_one[0:0] = [temp]
            elif to == 2:
                stack_two[0:0] = [temp]
            elif to == 3:
                stack_three[0:0] = [temp]
            elif to == 4:
                stack_four[0:0] = [temp]
            elif to == 5:
                stack_five[0:0] = [temp]
            elif to == 6:
                stack_six[0:0] = [temp]
            elif to == 7:
                stack_seven[0:0] = [temp]
            elif to == 8:
                stack_eight[0:0] = [temp]
            elif to == 9:
                stack_nine[0:0] = [temp]
        elif _from == 9:
            temp = stack_nine[0]
            stack_nine.remove(stack_nine[0])
            if to == 1:
                stack_one[0:0] = [temp]
            elif to == 2:
                stack_two[0:0] = [temp]
            elif to == 3:
                stack_three[0:0] = [temp]
            elif to == 4:
                stack_four[0:0] = [temp]
            elif to == 5:
                stack_five[0:0] = [temp]
            elif to == 6:
                stack_six[0:0] = [temp]
            elif to == 7:
                stack_seven[0:0] = [temp]
            elif to == 8:
                stack_eight[0:0] = [temp]
            elif to == 9:
                stack_nine[0:0] = [temp]
            break
print(stack_one[0])
print(stack_two[0])