from sys import stdin
lines = [str(line.strip()) for line in stdin.readlines()]
c, l = sum([len(line) for line in lines]), 0

for line in lines:
    l += len(rf"{repr(line)}")
    for i in range(len(line)):
        if line[i] == '"':
            l += 1
    
s = "\"\""
print(s)
print(repr(rf"{s}"))

print(l - c)
