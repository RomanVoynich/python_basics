num = int(input())
flag = True

while num != 0:
    a = num % 10
    num //= 10
    b = num % 10
    if not(a <= b) and b != 0:
        flag = False
if flag:
    print('YES')
else:
    print('NO')