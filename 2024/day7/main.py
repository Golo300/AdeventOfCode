
def readInput(f):
    input = {}
    for line in f:
        testValue, numbers = line.split(": ")
        numbers = [int(n) for n in numbers.split(" ")]
        input[int(testValue)] = numbers

    return input

def nextOperator(i, j , operator):
    result = 0
    if operator == "+":
        result = i + j
    elif operator == "*":
        result =  i * j
    elif operator == "|":
        result = int(str(i) + str(j))
    else:
        raise Exception(f"unsupported operator {operator}")
    if result < i:
        raise Exception(f"illegal operator {operator} result {result} must be gretter than input {i}")
    return result

def calibrate(numbers, testValue, i, currentValue, operators):
    if currentValue > testValue:
        return False
    if i >= len(numbers) - 1: # last value
        return currentValue == testValue

    i += 1
    nextValue = numbers[i]

    for operator in operators:
        nextCurrent = nextOperator(currentValue, nextValue, operator) 
        if calibrate(numbers, testValue, i, nextCurrent, operators):
            return True

    return False

        

def task1(input):

    sum = 0
    for testValue in input:
        numbers = input[testValue]
        result = calibrate(numbers, testValue, 0, numbers[0], ["+", "*"])
        if result:
            sum += testValue

    return sum

def task2(input):

    sum = 0
    for testValue in input:
        numbers = input[testValue]
        result = calibrate(numbers, testValue, 0, numbers[0], ["+", "*", "|"])
        if result:
            sum += testValue

    return sum

if __name__ == "__main__":
    print("Day 7")
    f = open("input", "r")
    input = readInput(f)

    result = task1(input)
    print(f"Part1: {result}")

    result = task2(input)
    print(f"Part2: {result}")
