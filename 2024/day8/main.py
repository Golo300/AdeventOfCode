
def readInput(f):
    matrix = []
    for line in f:
        line_array = []
        for n in line:
            if n == "\n":
                continue
            line_array.append(n)
        matrix.append(line_array)
    return matrix

def task1(matrix):
    frequenze = {}

    for y, line in enumerate(matrix):
        for x, n in enumerate(line):
            if n == ".":
                continue

            if n not in frequenze.keys():
                frequenze[n] = [(x, y)]
            else:
                frequenze[n].append((x, y))

    uniqueAntinodes = []
    for key in frequenze:

        for firstValue in frequenze[key]:
            for secondValue in frequenze[key]:
                if firstValue == secondValue:
                    continue
                x1, y1 = firstValue
                x2, y2 = secondValue
                dx, dy = x1 - x2, y1 - y2

                x1 += dx
                y1 += dy

                if x1 < 0 or x1 >= len(matrix[0]) or y1 < 0 or y1 >= len(matrix):
                    continue

                if (x1, y1) not in uniqueAntinodes:
                    uniqueAntinodes.append((x1, y1))
    
    return len(uniqueAntinodes)

def task2(matrix):
    frequenze = {}

    for y, line in enumerate(matrix):
        for x, n in enumerate(line):
            if n == ".":
                continue

            if n not in frequenze.keys():
                frequenze[n] = [(x, y)]
            else:
                frequenze[n].append((x, y))

    uniqueAntinodes = []
    for key in frequenze:

        for firstValue in frequenze[key]:
            for secondValue in frequenze[key]:
                if firstValue == secondValue:
                    continue
                x1, y1 = firstValue
                x2, y2 = secondValue
                dx, dy = x1 - x2, y1 - y2
                x1 += dx
                y1 += dy

                while not (x1 < 0 or x1 >= len(matrix[0]) or y1 < 0 or y1 >= len(matrix)):
                    if (x1, y1) not in uniqueAntinodes:
                        uniqueAntinodes.append((x1, y1))
                    x1 += dx
                    y1 += dy
    for key in frequenze:
        anntenas = frequenze[key]
        if len(anntenas) == 1:
            continue
        
        for x, y in anntenas:
            if (x, y) not in uniqueAntinodes:
                uniqueAntinodes.append((x, y))
    
    return len(uniqueAntinodes)

if __name__ == "__main__":
    print("Day 8")
    f = open("input", "r")
    matrix = readInput(f)

    result = task1(matrix)
    print(f"Task1: {result}")
    result = task2(matrix)
    print(f"Task2: {result}")
