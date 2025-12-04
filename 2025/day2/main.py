
def readInput(f):

    allRanges = []

    for line in f:
        ranges = line.split(",")
        for item in ranges:
            start, end = item.split("-")
            allRanges.append((int(start), int(end)))

    return allRanges

def getInvalidIDsum(ranges):

    result = 0

    for t in ranges:
        start, end = t
        for i in range(start, end + 1):
            w = str(i)
            if len(w) % 2 == 0:
                if w[:len(w)//2] == w[len(w)//2:]:
                    result += i

    return result

def getInvalidIDsumAll(ranges):

    result = 0

    for t in ranges:
        start, end = t
        for i in range(start, end + 1):

            w = str(i)
            found = False

            for r in range(1, len(w)):
                seq = w[:r]
                fail = False

                if len(w) % len(seq) != 0: continue
                for j in range(len(seq), len(w) - len(seq) + 1, len(seq)):
                    if seq != w[j:j + len(seq)]:
                        fail = True
                        break

                if fail: continue

                result += i
                break

    return result
if __name__ == "__main__":
    print("Day 1")
    f = open("input", "r")
    ranges = readInput(f)
    result = getInvalidIDsumAll(ranges)
    print(result)
