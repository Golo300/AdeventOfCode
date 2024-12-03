import re

number_debug_1 = []
number_debug_2 = []

def readInput(f):
    input = ""
    for line in f:
        input += line
    return input

def task1(input):
    sum = 0
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    output = re.findall(regex, input)
    if output:
        sum = 0
        for i, j in output:
            sum += int(i) * int(j)
    return sum

def task2(input):
    sum = 0

    dos_index = [m.start() for m in re.finditer(r"do\(\)", input)]
    donts_index = [m.start() for m in re.finditer(r"don't\(\)", input)]

    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    output_index = [m.start() for m in re.finditer(regex, input)]
    output = re.findall(regex, input)
    if not output:
        return

    state = True
    macht_counter = 0

    for i in range(0, len(input)):
        if i in dos_index:
            state = True
        if i in donts_index:
            state = False

        if i in output_index:
            if state:

                number_debug_2.append(int(output[macht_counter][0]))
                number_debug_2.append(int(output[macht_counter][1]))

                sum += int(output[macht_counter][0]) * int(output[macht_counter][1])
            macht_counter += 1
    return sum

# "\d" -> [0-9]
# "" -> any
automat = [
        {"m": 1, "d": 13},# 0
        {"u": 2},# 1
        {"l": 3},# 2
        {"(": 4},# 3

        {"#D": 5},# 4
        {"#D": 6, ",": 8},# 5
        {"#D": 7, ",": 8},# 6
        {",": 8},# 7

        {"#D": 9},# 8
        {"#D": 10, ")": 12},# 9
        {"#D": 11, ")": 12},# 10
        {")": 12},# 11
        {}, # 12

        {"o": 14},# 13
        {"n": 15},# 14
        {"'": 16},# 15
        {"t": 17},# 16
        {"(": 18},# 17
        {")": 19},# 18

        {"": 19, "d": 20},# 19
        {"": 19, "o": 21},# 20
        {"": 19, "(": 22},# 21
        {"": 19, ")": 0},# 22
        
        ]
start = 0
accepted = [ 12 ]


def iterateAutomat(a, start, accepted, input):
    sum = 0
    state = start
    first = True
    firstStr = ""
    secondStr = ""

    for i in input:
        if 4 <= state <= 11:
            if i == ",":
                first = False
            if i.isnumeric():
                if first:
                    firstStr += i
                else:
                    secondStr += i
        else:
            firstStr = ""
            secondStr = ""
            first = True

        inputStr = i
        if i.isnumeric():
            inputStr = "#D"

        if inputStr in a[state].keys():
            state = a[state][inputStr]
            if state in accepted and i == ")":
                number_debug_1.append(int(firstStr))
                number_debug_1.append(int(secondStr))
                sum += int(firstStr) * int(secondStr)
                state = 0
        elif "" in a[state].keys():
            state = a[state][""]
            if state in accepted and i == ")":
                number_debug_1.append(int(firstStr))
                number_debug_1.append(int(secondStr))
                sum += int(firstStr) * int(secondStr)
                state = 0
        else:
            state = 0
    return sum

if __name__ == "__main__":
    print("Day 3")
    f = open("input", "r")
    input = readInput(f)
    print(f"Part1: {task1(input)}")
    print(f"Part2: {task2(input)}")
    print(f"Part2 with help: {iterateAutomat(automat, start, accepted, input)}")
