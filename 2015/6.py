from sys import stdin
from tqdm import tqdm
import numpy as np

insts = stdin.readlines()
insts = [inst.strip().split() for inst in insts]

def compile(inst):
    if inst[1] == 'on' or inst[1] == 'off':
        a = list(map(int, inst[2].split(',')))
        b = list(map(int, inst[4].split(',')))
        return " ".join(inst[:2]), a, b
    else:
        a = list(map(int, inst[1].split(',')))
        b = list(map(int, inst[3].split(',')))
        return 'toggle', a, b

class Grid:

    def __init__(self):
        self.grid = np.array([[0] * 1000] * 1000)

    def execute(self, kind, a, b):
        xs, ys = self.__locate(a, b)
        for x in xs:
            for y in ys:
                if kind == 'turn on':
                    self.grid[x][y] += 1
                elif kind == 'turn off':
                    self.grid[x][y] = max(self.grid[x][y] - 1, 0)
                else:
                    self.grid[x][y] += 2

    def __str__(self):
        counts = 0
        for row in self.grid:
            for entry in row:
                if entry:
                    counts += entry
        return str(counts)
        
    def __locate(self, a, b):
        xs = [i for i in range(a[0], b[0] + 1)]
        ys = [i for i in range(a[1], b[1] + 1)]
        return xs, ys

grid = Grid()

for inst in tqdm(insts):
    kind, a, b = compile(inst)
    grid.execute(kind, a, b)

print(grid)
