from sys import stdin
import json


with open('12.txt', 'r') as f:
    data = json.load(f)
count = []


def func(iii):
    if type(iii) == list:
        ii = iii
    elif type(iii) == dict:
        ii = iii.values()
    if 'red' in ii and type(iii) == dict:
        return
    for i in ii:
        if type(i) == int:
            count.append(i)
        elif type(i) == list or type(i) == dict:
            func(i)
    

func(data)
print(sum(count))
