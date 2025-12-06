
def readInput(f):

    stillRange = True
    ranges = []
    ids = []

    for line in f:
        if line == "\n": 
            stillRange = False
            continue
        if stillRange:
            start, end =  line.split("-")
            ranges.append((int(start), int(end)))
        else:
            ids.append(int(line))

    return ranges, ids

def freshIds(ranges, ids):

    result = 0
    for id in ids:
        for range in ranges:
            start, end = range
            if start <= id <= end:
                result += 1
                break
    return result

def sortRanges(ranges):

    ranges = sorted(ranges, key=lambda tup: tup[0])
    return ranges

def merge(ranges):

    end = len(ranges)
    index = 0

    while index != len(ranges):
        print(ranges)
        print(index)
        if index + 1 == len(ranges):
            break

        start, end = ranges[index]
        nextRange = ranges[index + 1]

        if start <= nextRange[0] <= end:
            ranges[index] = (start, max(end, nextRange[1]))
            ranges.pop(index + 1)
            end -= 1
        else:
            index += 1

def freshIdsAll(ranges):
    
    ranges = sortRanges(ranges)
    mergeRange = merge(ranges)
    print(mergeRange)

    result = 0
    for range in ranges:
        start, end = range
        result += end - start + 1

    return result

if __name__ == "__main__":
    print("Day 1")
    f = open("input", "r")
    ranges, ids = readInput(f)
    result = freshIdsAll(ranges)
    print(result)
