



def readInput(f):
    group1 = []
    group2 = []

    for line in f:
        first, second = line.split("   ")
        group1.append(int(first))
        group2.append(int(second))

    return group1, group2

def calculateDistance(g1, g2):
    g1 = sorted(g1)
    g2 = sorted(g2)

    distance = 0

    for first, second in zip(g1, g2):
        distance += abs(first - second)

    return distance

def calculateSimilarity(g1, g2):
    sim = 0
    referenceMap = {}
    
    # build chache
    for second in g2:
        if second not in referenceMap:
            referenceMap[second] = 1
        else:
            referenceMap[second] += 1

    # calculate
    for first in g1:
        sim += first * (referenceMap.get(first) or 0)

    return sim

if __name__ == "__main__":
    print("Day 1")
    f = open("input", "r")
    g1, g2 = readInput(f)
    distance = calculateDistance(g1, g2)
    print(f"Solution first part: {distance}")

    sim = calculateSimilarity(g1, g2)
    print(f"Solution second part: {sim}")
