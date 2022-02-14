num = int(input())
a = num % 10
flag = True

while num != 0:
    last = num % 10
    num //= 10
    if a != last:
        flag = False

if flag:
    print('YES')
else:
    print('NO')


