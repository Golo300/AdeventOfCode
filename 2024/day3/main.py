import re

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
                sum += int(output[macht_counter][0]) * int(output[macht_counter][1])
            macht_counter += 1
    return sum

if __name__ == "__main__":
    print("Day 3")
    f = open("input", "r")
    input = readInput(f)
    print(f"Part1: {task1(input)}")
    print(f"Part2: {task2(input)}")
