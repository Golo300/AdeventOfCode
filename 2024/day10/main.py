from copy import deepcopy

def readInput(f):
    matrix = []
    for line in f:
        line_array = []
        for n in line:
            if n == "\n":
                continue
            line_array.append(int(n))
        matrix.append(line_array)
    return matrix

def breathSearch(nextNodes, visited, found):

    if len(nextNodes) == 0:
        return found

    vectors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    nextnextNodes = []

    for x, y in nextNodes:
        for dx, dy in vectors:

            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= len(matrix[0]) or ny < 0 or ny >= len(matrix):
                continue

            if matrix[ny][nx] == matrix[y][x] + 1 and [nx, ny] not in visited:
                nextnextNodes.append([nx, ny])
                visited.append([nx, ny])
                if matrix[ny][nx] == 9:
                    found += 1
    return breathSearch(nextnextNodes, visited, found)

def search(matrix):
    sum = 0

    for y, line in enumerate(matrix):
        for x, n in enumerate(line):

            if n == 0:
                nextsum= breathSearch([[x, y]], [], 0)
                sum += nextsum
    return sum

def backtracking(lastNode):

    x, y = lastNode
    found = 0
    if matrix[y][x] == 9:
        found += 1
        return found

    vectors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    for dx, dy in vectors:

        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= len(matrix[0]) or ny < 0 or ny >= len(matrix):
            continue

        if matrix[ny][nx] == matrix[y][x] + 1:
            found += backtracking([nx , ny])

    return found

def task2(matrix):
    sum = 0

    for y, line in enumerate(matrix):
        for x, n in enumerate(line):

            if n == 0:
                nextsum= backtracking([x, y])
                sum += nextsum
    return sum

if __name__ == "__main__":
    print("Day 10")
    f = open("input", "r")
    matrix = readInput(f)
    result= search(matrix)
    print(f"Task1 {result}")
    result= task2(matrix)
    print(f"Task2 {result}")
