num = int(input())

if 999 < num <= 9999:
    num = num
else:
    num = 1
    
if (num % 7 == 0) or (num % 17 == 0):
    print('YES')
else:
    print('NO')
