
def readInput(f):

    banks = []

    for line in f:
        banks.append([int(x) for x in list(line[:-1])])

    return banks

def findJoltage(banks):

    result = 0

    for bank in banks:
        globalMax = max(bank[:-1])

        indexMax = bank.index(globalMax)

        localMax = max(bank[indexMax + 1:])

        result += int(str(globalMax) + str(localMax))

    return result


def findJoltageSudo(banks):

    result = 0

    for bank in banks:

        numStr = ""
        startP = 0
        endPointer = len(bank) - 1

        for i in range(12):
            revers = 11 - i

            scop = bank[startP:endPointer + 1 - revers]
            nextMax = max(scop)
            numStr += str(nextMax)

            index = scop.index(nextMax)
            startP += index + 1
        
        result += int(numStr)

    return result

if __name__ == "__main__":
    print("Day 1")
    f = open("input", "r")
    banks = readInput(f)
    result = findJoltageSudo(banks)
    print(result)
