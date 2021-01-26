from sys import stdin
inp = [line.strip().split() for line in stdin.readlines()]
ccs = {line[0]: {} for line in inp}; ccs['Straylight'] = {}

for line in inp:
    ccs[line[0]][line[2]] = int(line[-1])
    ccs[line[2]][line[0]] = int(line[-1])

lens = []

def route(s, done, l):
    done.add(s)
    if len(ccs) == len(done):
        print(done)
        print(set(ccs.keys()))
        return l
    ps = sorted(ccs[s], key=ccs[s].__getitem__)
    ps = [p for p in ps if p not in done]
    t = ps[-1]; d = ccs[s][t]
    l += d
    return route(t, done, l)

for s in ccs.keys():
    done = set(); l=0
    l = route(s, done, l)
    lens.append(l)

print(max(lens))
