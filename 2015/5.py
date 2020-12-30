from sys import stdin

inputs = stdin.readlines()
inputs = [input.strip() for input in inputs]

def check(string):
    pnumb = 0
    pairs = []

    twice = 0

    for i in range(len(string)):
        # pair check
        if i > 1:
            pairs.append(string[i-2] + string[i-1])
        if i < len(string) - 1 and string[i] + string[i+1] in pairs:
            pnumb += 1
         
        # overlap check
        if i < len(string) - 2 and string[i] == string[i + 2]:
            twice += 1
        
    print(pairs)
    if twice > 0 and pnumb > 0:
        return 1
    else:
        return 0

count = 0
for string in inputs:
    count += check(string)

print(count)
