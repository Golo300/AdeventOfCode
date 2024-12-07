from copy import copy, deepcopy

def readInput(f):
    matrix = []
    start = [0, 0]
    possible = ["<", "^", ">", "v"]
    for y, line in enumerate(f):
        line_array = []
        for x, n in enumerate(line):
            line_array.append(n)
            if n in possible:
                start = [x, y]
        matrix.append(line_array)
    return start, matrix

def getDirVector(dir):
    dx, dy = 0, 0
    if dir == 0:
        dy = -1
        dx = 0
    if dir == 1:
        dy = 0
        dx = 1
    if dir == 2:
        dy = 1
        dx = 0
    if dir == 3:
        dy = 0
        dx = -1
    return dx, dy

def getDistance(matrix, start):

    uniqueobstruction= []
    dirArray = [ "^", ">", "v", "<",]
    x, y = start
    run = True
    dir = 0 # facing up
    reverser = 0
    while run:
        guard = matrix[y][x]

        if guard == "^":
            
            y -= 1
            if y < 0:
                run = False
                y += 1
            elif matrix[y][x] == "#":
                y += 1
                dir += 1
                dir %= len(dirArray)
                matrix[y][x] = dirArray[dir]
                
        elif guard == ">":
            
            x += 1
            if x >= len(matrix[0]):
                run = False
                x -= 1
            elif matrix[y][x] == "#":
                x -= 1
                dir += 1
                dir %= len(dirArray)
                matrix[y][x] = dirArray[dir]

        elif guard == "v":
            
            y += 1
            if y >= len(matrix):
                run = False
                y -= 1
            elif matrix[y][x] == "#":
                y -= 1
                dir += 1
                dir %= len(dirArray)
                matrix[y][x] = dirArray[dir]

        elif guard == "<":
            
            x -= 1
            if x < 0:
                run = False
                x += 1
            elif matrix[y][x] == "#":
                x += 1
                dir += 1
                dir %= len(dirArray)
            else:
                matrix[y][x] = "X"

        matrix[y][x] = dirArray[dir]

    sum = 0
    for line in matrix:
        for n in line:
            if n not in ["#", ".", "\n"]:
                sum += 1

    for x, y in uniqueobstruction:
        matrix[y][x] = "O"
    return sum, reverser


if __name__ == "__main__":
    print("Day 6")
    f = open("example_input", "r")
    start, matrix = readInput(f)
    sum, reverser = getDistance(matrix, start)
    print(f"Part1: {sum}")
    for line in matrix:
        print(line)
