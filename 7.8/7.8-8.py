num = int(input())
num //= 2

for i in range(1, num + 2):
    for j in range(i):
        print('*', end='')
    print()

for i in range(1, num + 2):
    for j in range(num + 1, i, -1):
        print('*', end='')
    print()
