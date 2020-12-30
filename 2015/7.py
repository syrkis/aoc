from sys import stdin
opps = [opp.strip().split() for opp in stdin.readlines()]
opps2 = [['956', '->', 'b']]
for i in range(len(opps)):
    if opps[i][-1] != 'b':
        opps2.append(opps[i])

C = {}; M = set()

def interp(opp):
    target = opp[-1]
    units = [unit for unit in opp[:-1] if unit.islower()]
    if set(units).intersection(M) == set(units):
        if len(opp) == 3:
            if opp[0].isnumeric():
                C[target] = int(opp[0])
            else:
                C[target] = C[opp[0]]
        elif opp[0].isnumeric():
            C[target] = int(opp[0]) & C[opp[2]]
        elif opp[0].islower():
            if opp[1] == 'AND':
                C[target] = C[opp[0]] & C[opp[2]]
            elif opp[1] == 'OR':
                C[target] = C[opp[0]] | C[opp[2]]
            elif opp[1] == 'RSHIFT':
                C[target] = C[opp[0]] >> int(opp[2])
            else:
                C[target] = C[opp[0]] << int(opp[2])
        else:
            C[target] = ~ C[opp[1]]
        M.add(opp[-1])

while len(M) < len(opps2):
    for opp in opps2:
        interp(opp)

print(C['a'])
