
def readInput(f):
    matrix = []
    for line in f:
        line_array = []
        for n in line:
            line_array.append(str(n))
        matrix.append(line_array)
    return matrix


def findDir(matrix, s, x, y, dx, dy):

    for chr in s:
        if x < 0 or y < 0:
            return False
        if x >= len(matrix[0]) or y >= len(matrix):
            return False
        if matrix[y][x] != chr:
            return False
        x += dx
        y += dy

    return True

def countX(matrix):
    count = 0

    for y, line in enumerate(matrix):
        for x, char in enumerate(line):
            if char == "A":
                if x > 0 and x < len(line) - 1 and y > 0 and y < len(matrix) - 1:
                    leftUp = matrix[y - 1][x - 1]
                    rightUp = matrix[y - 1][x + 1]
                    leftDown = matrix[y + 1][x - 1]
                    rightDown = matrix[y + 1][x + 1]

                    if not all(e == "M" or e == "S" for e in [leftUp, rightUp, leftDown, rightDown]):
                        continue

                    if leftUp != rightDown and rightUp != leftDown:
                        count += 1
    return count

def countString(matrix, s):
    if len(s) == 0:
        return
    count = 0

    for y, line in enumerate(matrix):
        for x, char in enumerate(line):
            if char == s[0]:
                if findDir(matrix, s, x, y, 0, 1): count +=1
                if findDir(matrix, s, x, y, 1, 0): count +=1
                if findDir(matrix, s, x, y, 0, -1): count +=1
                if findDir(matrix, s, x, y, -1, 0): count +=1
                if findDir(matrix, s, x, y, 1, 1): count +=1
                if findDir(matrix, s, x, y, -1, 1): count +=1
                if findDir(matrix, s, x, y, 1, -1): count +=1
                if findDir(matrix, s, x, y, -1, -1): count +=1
    return count


if __name__ == "__main__":
    print("Day 3")
    f = open("input", "r")
    matrix = readInput(f)
    result = countString(matrix, "XMAS")
    print(f"Part 1: {result}")
    result = countX(matrix)
    print(f"Part 2: {result}")

