from sys import stdin
data = [d.strip().split() for d in stdin.readlines()]
ds = {d[2] : {} for d in data}
ls = set()
for line in data:
    ds[line[0]] = {}

for line in data:
    ds[line[0]][line[2]] = int(line[-1])
    ds[line[2]][line[0]] = int(line[-1])

def step(s, vis, n):
    if len(vis) == len(set(ds.keys())):
        return n
    t = sorted([(k, v) for k, v in ds[s].items() if k not in vis], key = lambda x: x[1])[::-1]
    print(t)
    t = t[0][0]
    vis.add(t)
    return step(t, vis, n + ds[s][t])
    

for k in ds.keys():
    vis = set()
    vis.add(k)
    ls.add(step(k, vis, 0))

print(max(ls))
