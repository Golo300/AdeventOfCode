from copy import deepcopy

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

def breathSearch(matrix, nextNodes, t, area, edges, i):

    if len(nextNodes) == 0:
        return area, edges

    vectors = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
    nextnextNodes = []

    edge = 4 * len(nextNodes)
    for x, y in nextNodes:
        for dx, dy in vectors:

            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= len(matrix[0]) or ny < 0 or ny >= len(matrix):
                continue

            if matrix[ny][nx] == t:
                matrix[ny][nx] = i
                if dx != 0 or dy != 0:
                    nextnextNodes.append([nx, ny])
                area += 1

            if dx != 0 or dy != 0:
                if matrix[ny][nx] == t or matrix[ny][nx] == i:
                    edge -= 1
    edges += edge

    return breathSearch(matrix, nextnextNodes, t, area, edges, i)

def task1(matrix):
    result = 0
    i = 0

    for y, line in enumerate(matrix):
        for x, n in enumerate(line):
            if type(matrix[y][x]) == int:
                continue
            area, edges = breathSearch(matrix, [[x, y]], n, 0, 0, i)
            result += area * edges
            i += 1
    return result

if __name__ == "__main__":
    print("Day 12")
    f = open("input", "r")
    matrix = readInput(f)
    result = task1(matrix)
    print(f"task1 {result}")
