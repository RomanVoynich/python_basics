a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a <= b:
    x1 = a
else:
    x1 = b

if c <= d:
    x2 = c
else:
    x2 = d

if x1 <= x2:
    print(x1)
else:
    print(x2)
