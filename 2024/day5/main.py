
def readInput(f):
    foundMap = {}
    reverseIndex = {}

    isDef = True
    arrays = []

    for line in f:
        if line == "\n":
            isDef = False
            continue
        if isDef:
            first, second = line.split("|")
            first = int(first)
            second = int(second)
            foundMap[first] = False
            if second not in reverseIndex:
                reverseIndex[second] = [ first ]
            else:
                reverseIndex[second].append(first)

        else:
            array = [int(e) for e in line.split(",")]
            arrays.append(array)

    return foundMap, reverseIndex, arrays

def task1(foundMap, reverseIndex, arrays):
    sum = 0
    failing = []

    for array in arrays:
        for n in array:

            if n in foundMap:
                foundMap[n] = True
            if n in reverseIndex:
                failed = False
                for p in reverseIndex[n]:
                    if not foundMap[p] and p in array:
                        failed = True
                        failing.append(array)
                        break
                if failed: break

        else:
            sum += array[len(array)//2]

        foundMap = {key: False for key in foundMap.keys()}
    return sum, failing

def isValid(foundMap, reverseIndex, array):
    foundMap = {key: False for key in foundMap.keys()}
    for n in array:

        if n in foundMap:
            foundMap[n] = True
        if n in reverseIndex:
            failed = False
            for p in reverseIndex[n]:
                if not foundMap[p] and p in array:
                    return False
            if failed: break

    return True

def correctFailing(foundMap, reverseIndex, farray):
    while not isValid(foundMap, reverseIndex, farray):
        foundMap = {key: False for key in foundMap.keys()}

        for i, n in enumerate(farray):
            failed = False
            if n in foundMap:
                foundMap[n] = True
            if n in reverseIndex:
                for p in reverseIndex[n]:
                    if not foundMap[p] and p in farray:
                        swapIndex = farray.index(p, i + 1)
                        farray[i] = p
                        farray[swapIndex] = n # must be first index since linear search
                        failed = True
                        break
                if failed: break
            if failed: break

def task2(foundMap, reverseIndex, failingArrays):
    sum = 0
    for farray in failingArrays:
        correctFailing(foundMap, reverseIndex, farray)
        sum += farray[len(farray)//2]
    return sum


if __name__ == "__main__":
    print("Day 3")
    f = open("input", "r")
    foundMap, reverseIndex, arrays = readInput(f)
    result, failing = task1(foundMap, reverseIndex, arrays)
    print(f"Solution Part1: {result}")
    result = task2(foundMap, reverseIndex, failing)
    print(f"Solution Part2: {result}")

