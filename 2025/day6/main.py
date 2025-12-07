
def readInput(f):

    matrix = []

    for line in f:
        matrix.append([x for x in line.split()])

    matrix[:-1] = [[int(x) for x in row] for row in matrix[:-1]]
    
    return matrix

def readInputRaw(f):

    matrix = []

    for line in f:
        matrix.append(line)

    operators = [x for x in matrix[-1].split()]
    
    return matrix[:-1], operators

def calculate(matrix):
    result = 0
    for i in range(len(matrix[0])):
        operator = matrix[-1][i]
        columnsResult = 0 if operator == "+" else 1
        for j in range(len(matrix) - 1):
            value = matrix[j][i]
            if operator == "*":
                columnsResult *= value
            else:
                columnsResult += value
        result += columnsResult

    return result

def calculateAll(matrix, operators):
    result = 0

    for i in range(3):
        matrix = list(zip(*matrix[::-1]))

    matrix = ["".join(row) for row in matrix]
    matrix = matrix[1:]

    column = 1
    operator = operators[len(operators) - column]
    columnsResult = 0 if operator == "+" else 1

    for c in matrix:
        if c.strip() == "":
            column += 1
            operator = operators[len(operators) - column]
            result += columnsResult
            columnsResult = 0 if operator == "+" else 1
            continue
        value = int(c)
        if operator == "*":
            columnsResult *= value
        else:
            columnsResult += value
    result += columnsResult
    return result

if __name__ == "__main__":
    print("Day 1")
    f = open("input", "r")
    matrix, operators = readInputRaw(f)
    result = calculateAll(matrix, operators)
    print(result)
