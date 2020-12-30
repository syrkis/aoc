from sys import stdin

seq = [mov for mov in stdin.readline().strip()]
santa = {'0 0': 1}
robos = {'0 0': 1}
pos = [0, 0]

def trans(mov):
    if mov == '<':
        return -1, 0
    elif mov == '>':
        return 1, 0
    elif mov == 'v':
        return 0, -1
    else:
        return 0, 1

sh = 0; sv = 0
rh = 0; rv = 0

for i in range(len(seq)):
    upd = trans(seq[i])
    if i % 2 == 0: 
        sh += upd[0]
        sv += upd[1]
        key = "".join(str(sh) + ' ' + str(sv))
        if key not in santa:
            santa[key] = 1
        else:
            santa[key] += 1
    if i % 2 == 1:
        rh += upd[0]
        rv += upd[1]
        key = "".join(str(rh) + ' ' + str(rv))
        if key not in robos:
            robos[key] = 1
        else:
            robos[key] += 1

out = [entry for entry in santa]
for entry in robos:
    out.append(entry)

print(len(out))
print(len(set(out)))
