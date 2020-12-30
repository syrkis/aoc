from sys import stdin

seq = stdin.readline().strip()
seq = [1 if i == '(' else -1 for i in seq]
state = 0
count = 1
for i in seq:
    state += int(i)
    count += 1
    if state == -1:
        print(count)
        break

print(len(seq))
