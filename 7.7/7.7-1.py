mx = 0
s = 0

for i in range(10):          # 11
    x = int(input())
    if x < 0:
        s = s + x            # s = x
        if x >= mx:               # x > mx
            mx = x

if s < 0:
    print(s)
    print(mx)
else:
    print('NO')
