from sys import stdin
from tqdm import tqdm
from itertools import combinations

data = stdin.readlines()
data = [d.split() for d in data]
places = set([d[0] for d in data])
places.add(data[-1][2])
D = {place: {} for place in places}
routes = []

for line in data:
    D[line[0]][line[2]] = int(line[-1])
    D[line[2]][line[0]] = int(line[-1])

def router(dons, pots):
    if len(pots) == 1:
        dons.append(pots[0])
        routes.append(dons)
    for d in pots:
        d_tmp = dons + [d]
        p_tmp = [p for p in pots if p != d] 
        router(d_tmp, p_tmp)

dons = []
pots = list(places)
router(dons, pots)
lens = []

for route in tqdm(routes):
    l = 0
    for i in range(len(route) - 1):
        l += D[route[i]][route[i+1]]
    lens.append(l)

print(max(lens))
