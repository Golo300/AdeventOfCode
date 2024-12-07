from enum import Enum
from copy import deepcopy

def readInput(f):
    matrix = []
    start = [0, 0]
    possible = ["<", "^", ">", "v"]
    for y, line in enumerate(f):
        line_array = []
        for x, n in enumerate(line):
            if n == "\n":
                continue
            line_array.append(n)
            if n in possible:
                start = [x, y]
        matrix.append(line_array)
    return start, matrix

class Direction(Enum):

    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

    @staticmethod
    def toVector(dir):
        if dir == Direction.UP:
            return 0, -1
        if dir == Direction.LEFT:
            return -1, 0
        if dir == Direction.DOWN:
            return 0, 1
        if dir == Direction.RIGHT:
            return 1, 0
        return 0, 0

dirDefinition = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
dirString = {Direction.UP: "^", Direction.RIGHT: ">", Direction.DOWN: "v", Direction.LEFT: "<"}

def checkForCycle(pos, map) -> bool:
    startX = pos.x
    startY = pos.y
    startDir = pos.dir
    pos2 = Position(startX, startY, startDir)

    while not pos.outOfMap and not pos2.outOfMap:
        pos2.nextStep(map)
        if pos2 == pos:
            return True
        pos2.nextStep(map)
        if pos2 == pos:
            return True
        pos.nextStep(map)
        if pos2 == pos:
            return True
    return False

class Position:

    def __init__(self, x: int, y: int, dir: Direction) -> None:
        self.x = x
        self.y = y
        self.startX = x
        self.startY = y
        self.startDir = dir
        self.dir = dir
        self.outOfMap = False
        self.obstructions = 0
        self.obsticals = [(x, y)]

    def nextStep(self, map: list, top = False):
        if self.x < 0 or self.x >= len(map[0]) or self.y < 0 or self.y >= len(map):
            return

        dx, dy = Direction.toVector(self.dir)

        if self.x + dx < 0 or self.x + dx >= len(map[0]) or self.y + dy < 0 or self.y + dy >= len(map):
            self.outOfMap = True
            return
        
        map[self.y][self.x] = "Z"

        if map[self.y + dy][self.x + dx] == "#":
            self.rotateRight()
            return

        if top and not (self.x + dx, self.y + dy) in self.obsticals:

            copy = deepcopy(map)
            copy[self.y + dy][self.x + dx] = "#"

            if checkForCycle(Position(self.startX, self.startY, self.startDir), copy):
                self.obstructions += 1
                self.obsticals.append((self.x + dx, self.y + dy))

        self.x += dx
        self.y += dy

    
    def rotateRight(self):
        i = dirDefinition.index(self.dir)
        i += 1
        i %= len(dirDefinition)
        self.dir = dirDefinition[i]

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.dir == other.dir
        
def getReverse(pos, map):
    while not pos.outOfMap:
        pos.nextStep(map, True)

    for x, y in pos.obsticals:
        map[y][x] = "O"

if __name__ == "__main__":
    print("Day 6")
    f = open("input", "r")
    start, map = readInput(f)

    x, y = start
    pos = Position(x, y, Direction.UP)
    getReverse(pos, map)
    print(f"solution: {pos.obstructions}")
