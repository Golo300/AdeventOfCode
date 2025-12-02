
SIZE = 100

def readInput(f):

    instructions = []

    for line in f:
        instructions.append(line)

    return instructions

def crackDoor(instructions, start = 50):
    value = start
    counter = 0

    for i in instructions:
        
        dir = i[0]
        amount = int(i[1:])

        if dir == "L":
            value -= amount
        if dir == "R":
            value += amount

        value %= SIZE
        if value == 0: counter += 1

    return counter

def crackDoorNewMethod(instructions, start = 50):
    value = start
    counter = 0

    for i in instructions:
        
        dir = i[0]
        amount = int(i[1:])

        if dir == "L":
            for i in range(1, amount + 1):
                value -= 1
                value %= SIZE
                if value == 0:
                    counter += 1
        if dir == "R":
            for i in range(1, amount + 1):
                value += 1
                value %= SIZE
                if value == 0:
                    counter += 1
        value %= SIZE
    return counter


if __name__ == "__main__":
    print("Day 1")
    f = open("input", "r")
    instructions = readInput(f)
    print(crackDoorNewMethod(instructions))

