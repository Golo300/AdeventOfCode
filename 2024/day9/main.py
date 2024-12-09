
def readInput(f):
    numbers = []
    for line in f:
        for n in line:
            if n == "\n":
                continue
            numbers.append(int(n))
    return numbers

def task1(input):
    unzip = []

    index = 0
    isFree = False
    result = 0
    for number in input:

        if not isFree:
            for _ in range(number):
                unzip.append(index)
            index += 1

        else:
            for _ in range(number):
                unzip.append(-1)
        isFree = not isFree
    
    print(unzip)

    p1, p2 = 0, len(unzip) - 1

    while p1 < p2:
        if unzip[p1] == -1:
            unzip[p1] = unzip[p2]
            unzip[p2] = -1
            p2 -= 1
        else:
            p1 += 1

    print(unzip)

    for i, n in enumerate(unzip):
        if n != -1:
            result += i * n
    return result

def task2(input):
    unzip = []

    index = 0
    isFree = False
    result = 0
    for number in input:

        if not isFree:
            for _ in range(number):
                unzip.append(index)
            index += 1

        else:
            for _ in range(number):
                unzip.append(-1)
        isFree = not isFree

    for i in reversed(range(index)):
        indices = [k for k, x in enumerate(unzip) if x == i ]

        startFree, endFree = -1, -1
        for f, n in enumerate(unzip):
            if f > indices[0]:
                break
            
            if unzip[f] == -1:
                if startFree == -1:
                    startFree = f
            else:
                if startFree != -1 and endFree == -1:
                    endFree = f

                    space = endFree - startFree

                    if space >= len(indices):
                        for ind in indices:
                            unzip[ind] = -1
                        count = 0
                        for freeInd in range(startFree, endFree):
                            if count < len(indices):
                                unzip[freeInd] = i
                            count += 1
                        break
                    else:
                        startFree, endFree = -1, -1

    for i, n in enumerate(unzip):
        if n != -1:
            result += i * n
    return result
if __name__ == "__main__":
    print("Day 9")
    f = open("input", "r")
    input = readInput(f)
    result = task1(input)
    print(f"task1 {result}")
    result = task2(input)
    print(f"task2 {result}")
