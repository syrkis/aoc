pp = 'hxbxwxba'
alpha = 'abcdefghijklmnopqrstuvwxyz'
integ = {i: alpha[i] for i in range(len(alpha))}
alpha = {alpha[i] : i for i in range(len(alpha))}

def next(pp):
    pp = [p for p in pp]
    for i in range(len(pp)):
        if pp[i] != 'z':
            pp[i] = integ[alpha[pp[i]] + 1]
            return "".join(pp)
        else:
            pp[i] = 'a'
            return "".join(pp[i] + next(pp[i+1:]))

def cond1(pp):
    for i in range(len(pp) - 2):
        ss = alpha[pp[i]]
        if ss + 2 <= 24 and pp[i + 1] == integ[ss + 1] and pp[i + 2] == integ[ss + 2]:
            return True
    return False

def cond2(pp):
    pp = set([p for p in pp])
    nn = set(['i', 'o', 'l'])
    for p in pp:
        if p in nn:
            return False
    return True

def cond3(pp):
    ps = []
    for i in range(len(pp) - 1):
        fs = pp[i] + pp[i+1]
        if fs[0] == fs[1] and fs not in ps:
            ps.append(fs)
    return True if len(ps) >= 2 else False

def condition(pp):
    if cond2(pp) and cond1(pp) and cond3(pp):
        return True
    else:
        return False
i = 0
while not condition(pp):
    pp = next(pp[::-1])[::-1]
    print(pp, i, cond1(pp), cond2(pp), cond3(pp), sep='\t')
    i += 1
