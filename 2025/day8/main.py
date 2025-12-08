import math
from itertools import combinations

def readInput(f):

    corList = []

    for line in f:
        corList.append(tuple([int(x) for x in line.split(",")]))

    return corList

def d(cor1, cor2):
    x1, y1, z1 = cor1
    x2, y2, z2 = cor2

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def findPar(corList):
    result = 1

    circuts = []
    corIndex = {}# cor -> circut

    pairs = [] # [distance, cor1, cor2]

    
    for combo in combinations(corList, 2):
        cor1, cor2 = combo
        pairs.append([d(cor1, cor2), cor1, cor2])
    
    sortedPairs = sorted(pairs, key=lambda l: l[0])

    used = []
    limit = 1000
    for i, pair in enumerate(sortedPairs):
        if i == limit: break
        dis, cor1, cor2 = pair

        if cor1 not in used and cor2 not in used:
            newCircut = [cor1, cor2]
            circuts.append(newCircut)
            corIndex[cor1] = newCircut
            corIndex[cor2] = newCircut
            used.append(cor1)
            used.append(cor2)

        elif cor1 in used and cor2 not in used:
            corIndex[cor1].append(cor2)
            corIndex[cor2] = corIndex[cor1]
            used.append(cor2)
            for cor in corIndex[cor1]:
                corIndex[cor] = corIndex[cor1]

        elif cor2 in used and cor1 not in used:
            corIndex[cor2].append(cor1)
            corIndex[cor1] = corIndex[cor2]
            for cor in corIndex[cor2]:
                corIndex[cor] = corIndex[cor2]
            used.append(cor1)
        else:
            # merge
            if corIndex[cor1] == corIndex[cor2]: continue
            if corIndex[cor2] not in circuts:
                print(cor1, cor2)
                print()
                print(corIndex[cor1])
                print()
                print(corIndex[cor2])
                print()
                for c in circuts:
                    print(c)

            corIndex[cor1].extend(corIndex[cor2])
            circuts.remove(corIndex[cor2])
            corIndex[cor2] = corIndex[cor1]
            for cor in corIndex[cor1]:
                corIndex[cor] = corIndex[cor1]


    for c in circuts:
        print(c)
    print()
    for key in corIndex:
        if corIndex[key] not in circuts:
            print(key, corIndex[key])

    lenList = []
    for circut in circuts:
        lenList.append(len(circut))

    lenList.sort(reverse=True)
    for i in range(3):
        result *= lenList[i]

    return result

def findLoop(corList):
    result = 1

    circuts = []
    corIndex = {}# cor -> circut

    pairs = [] # [distance, cor1, cor2]

    
    for combo in combinations(corList, 2):
        cor1, cor2 = combo
        pairs.append([d(cor1, cor2), cor1, cor2])
    
    sortedPairs = sorted(pairs, key=lambda l: l[0])

    used = []
    lastPair = [(0,0,0), (0,0,0)]
    for i, pair in enumerate(sortedPairs):
        if len(circuts) == 1 and len(circuts[0]) == len(corList):
            break
        lastPair = pair
        dis, cor1, cor2 = pair

        if cor1 not in used and cor2 not in used:
            newCircut = [cor1, cor2]
            circuts.append(newCircut)
            corIndex[cor1] = newCircut
            corIndex[cor2] = newCircut
            used.append(cor1)
            used.append(cor2)

        elif cor1 in used and cor2 not in used:
            corIndex[cor1].append(cor2)
            corIndex[cor2] = corIndex[cor1]
            used.append(cor2)
            for cor in corIndex[cor1]:
                corIndex[cor] = corIndex[cor1]

        elif cor2 in used and cor1 not in used:
            corIndex[cor2].append(cor1)
            corIndex[cor1] = corIndex[cor2]
            for cor in corIndex[cor2]:
                corIndex[cor] = corIndex[cor2]
            used.append(cor1)
        else:
            # merge
            if corIndex[cor1] == corIndex[cor2]: continue
            if corIndex[cor2] not in circuts:
                print(cor1, cor2)
                print()
                print(corIndex[cor1])
                print()
                print(corIndex[cor2])
                print()
                for c in circuts:
                    print(c)

            corIndex[cor1].extend(corIndex[cor2])
            circuts.remove(corIndex[cor2])
            corIndex[cor2] = corIndex[cor1]
            for cor in corIndex[cor1]:
                corIndex[cor] = corIndex[cor1]

    print("Result", lastPair)
    dis, cor1, cor2 = lastPair
    result = cor1[0] * cor2[0]

    return result

if __name__ == "__main__":
    print("Day 1")
    f = open("input", "r")
    corList = readInput(f)
    result = findLoop(corList)
    print(result)
