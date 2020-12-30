import hashlib

key = 'yzbqklnj'
n = 282749
while True:
    if n % 1000000 == 0:
        print('X')
    target = hashlib.md5((key + str(n)).encode())
    if str(target.hexdigest())[:6] == '000000':
        break
    n += 1

print(n)
    
