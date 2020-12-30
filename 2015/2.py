from sys import stdin

data = stdin.readlines()
data = [entry.strip().split('x') for entry in data]

def ribon(h, w, l):
    h, w, l = list(map(int, [h, w, l]))
    hwl = sorted([h, w, l])
    rib = hwl[0] * 2 + hwl[1] * 2 + h * w * l
    return rib

counter = 0

for entry in data:
    counter +=  ribon(entry[0], entry[1], entry[2])

print(counter)

