dd = [int(d) for d in '3113322113']

def las(dd):
    c = [dd[0]]
    g = [1]
    for i in range(1, len(dd)):
        if dd[i] == c[-1]:
            g[-1] = g[-1] + 1
        else:
            g.append(1)
            c.append(dd[i])
    out = "".join(["".join([str(i[0]), str(i[1])]) for i in list(zip(g, c))])
    return out
    

for i in range(50):
    dd = las(dd)
print(len(dd))
