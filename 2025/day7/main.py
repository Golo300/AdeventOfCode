
def readInput(f):

    matrix = []

    for line in f:
        matrix.append(list(line)[:-1])

    return matrix

def calculateBeam(matrix):
    result = 0

    bx, by = matrix[0].index('S'), 0
    beamEnd = [[bx, by]]

    for y in range(len(matrix) - 1):
        print(y)
        print(beamEnd)
        nextBeamList = []
        for beam in beamEnd:
            bx, by = beam
            nextFiled = matrix[by + 1][bx]

            if nextFiled == "^":

                result += 1
                if [bx - 1, by + 1] not in nextBeamList:
                    nextBeamList.append([bx - 1, by + 1])

                if [bx + 1, by + 1] not in nextBeamList:
                    nextBeamList.append([bx + 1, by + 1])
            else:
                if [bx, by + 1] not in nextBeamList:
                    nextBeamList.append([bx, by + 1])

        beamEnd = nextBeamList

    print(len(beamEnd))
    return result

def calculateBeamTimeline(matrix):
    result = 0

    bx, by = matrix[0].index('S'), 0
    beamEnd = [[bx, by]]
    timelines = 0

    for y in range(len(matrix) - 1):
        nextBeamList = []
        for beam in beamEnd:
            bx, by = beam
            nextFiled = matrix[by + 1][bx]

            if nextFiled == "^":

                result += 1
                if [bx - 1, by + 1] not in nextBeamList:
                    nextBeamList.append([bx - 1, by + 1])

                if [bx + 1, by + 1] not in nextBeamList:
                    nextBeamList.append([bx + 1, by + 1])

            else:
                if [bx, by + 1] not in nextBeamList:
                    nextBeamList.append([bx, by + 1])

        beamEnd = nextBeamList

    return timelines


cache = {}
def recurive(matrix, x, y):

    for i in range(y, len(matrix)):
        if (i, x) in cache.keys():
            return cache[(i, x)]
        if matrix[i][x] == "^":
            result =  recurive(matrix, x + 1, i) + recurive(matrix, x - 1, i) + 1
            cache[(i, x)] = result
            return result

    return 0

if __name__ == "__main__":
    print("Day 1")
    f = open("input", "r")
    matrix = readInput(f)
    result = recurive(matrix, matrix[0].index('S'), 0) + 1
    print(result)
