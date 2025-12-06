
def readInput(f):

    matrix = []

    for line in f:
        matrix.append([x for x in list(line)])

    return matrix

def isInBound(x, y, matrix) -> bool:
    return 0 <= y < len(matrix) and 0 <= x < len(matrix[0])

def getSourund(x, y, matrix) -> int:
    result = 0 
    for dx in range(-1, 2):
       for dy in range(-1, 2):
           if (dx == 0 and dy == 0) or not isInBound(x + dx, y + dy, matrix): continue
           if matrix[y + dy][x + dx] == "@":
               result += 1

    return result

def findRolls(matrix):

    result = 0

    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == "@":
                if getSourund(x, y, matrix) < 4:
                    result += 1
    return result

def findRollsAll(matrix):
    
    result = 0
    end = False
    
    while not end:
        roundResult = 0
        matrixCopy = [row[:] for row in matrix]

        for y, row in enumerate(matrix):
            for x, char in enumerate(row):
                if char == "@":
                    if getSourund(x, y, matrix) < 4:
                        roundResult += 1
                        matrixCopy[y][x] = "0"

        result += roundResult
        matrix = matrixCopy
        if roundResult == 0:
            end = True
    return result

if __name__ == "__main__":
    print("Day 1")
    f = open("input", "r")
    matrix = readInput(f)
    result = findRollsAll(matrix)
    print(result)
