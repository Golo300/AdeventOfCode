
def readInput(f):
    matrix = []
    for line in f:
        line_array = []
        for n in line.split(" "):
            line_array.append(int(n))
        matrix.append(line_array)
    return matrix

def getSafeReports(matrix) -> int:
    safe = 0
    for line in matrix:
        dir = 0
        for i in range(len(line) - 1):
            diff = line[i] - line[i + 1]
            if not (1 <= abs(diff) <= 3):
                break
            
            if dir == 0:
                if diff > 0: dir = 1
                if diff < 0: dir = -1
            else:
                if diff > 0 and dir < 0:
                    break
                if diff < 0 and dir > 0:
                    break
        else:
            safe += 1

    return safe

def getSafeReportsOptimize(matrix, threshold) -> int:
    safe = 0
    for line in matrix:
        dir = 0
        first_diff = line[0] - line[1] # hope there is not input length 1
        if first_diff > 0: dir = 1
        if first_diff < 0: dir = -1
        hit = 0
        cur_len = len(line) - 1
        jump = - 1
        for i in range(cur_len):
            if jump == i:
                continue
            correct = checkDiff(line[i], line[i + 1], dir)
            if not correct:
                hit += 1
                jump = i + 1
                if i >= cur_len - 1:
                    break
                correctJump = checkDiff(line[i], line[i + 2], dir)
                if not correctJump:
                    hit += 1
        if hit <= threshold:
            safe += 1

    return safe

def checkDiff(first, second, dir):
    bad = False
    diff = first - second

    if not (1 <= abs(diff) <= 3):
        bad = True
    
    else:
        if diff > 0 and dir < 0:
            bad = True
        if diff < 0 and dir > 0:
            bad = True
    return not bad

if __name__ == "__main__":
    print("Day 2")
    f = open("input", "r")
    matrix = readInput(f)

    safeReports = getSafeReportsOptimize(matrix, 0)
    safeReportsOptimze = getSafeReportsOptimize(matrix, 1)
    print(f"Solution part1: {safeReports}")

    safeReports = getSafeReports(matrix)
    print(f"Solution part2: {safeReportsOptimze}")
