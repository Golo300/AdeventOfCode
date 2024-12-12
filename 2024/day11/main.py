from copy import deepcopy

def readInput(f):
    line = []
    line = [int(x) for x in f.readline().split(" ")]
    return line

def nextStep(line):
    toInsert = {}
    for i, n in enumerate(line):
        if n == 0:
            line[i] = 1
        elif len(str(n)) % 2 == 0:
            strN = str(n)
            firsHalf, secondHalf = strN[:len(strN)//2], strN[len(strN)//2:]
            line[i] = int(firsHalf)
            toInsert[i + 1] = int(secondHalf)
        else:
            line[i] = 2024 * n

    for key in toInsert:
        value = toInsert[key]
        line.insert(key, value)

def task2(line, n):
    map = {}

    for entry in line:
        map[entry] = 1

    for i in range(n):
        nextMap = deepcopy(map)
        for key in map:
            value = map[key]
            if key == 0:
                nextMap[key] -= 1 * value
                if 1 in nextMap:
                    nextMap[1] += 1 * value
                else:
                    nextMap[1] = 1
            elif len(str(key)) % 2 == 0:
                strN = str(key)
                firsHalf, secondHalf = int(strN[:len(strN)//2]), int(strN[len(strN)//2:])
                nextMap[key] -= 1 * value
                if firsHalf in nextMap:
                    nextMap[firsHalf] += 1 * value
                else:
                    nextMap[firsHalf] = 1 * value

                if secondHalf in nextMap:
                    nextMap[secondHalf] += 1 * value
                else:
                    nextMap[secondHalf] = 1 * value
                
            else:
                nextMap[key] -= 1 * value
                nextKey = 2024 * key
                if nextKey in nextMap:
                    nextMap[nextKey] += 1 * value
                else:
                    nextMap[nextKey] = 1 * value
        map = nextMap

    result = 0
    for key in map:
        value = map[key]
        result += value
    return result


def task1(line, n):
    for i in range(n):
        nextStep(line)
    return len(line)


if __name__ == "__main__":
    print("Day 11")
    f = open("input", "r")
    line = readInput(f)
    result = task2(line, 1000)
    print(result)
