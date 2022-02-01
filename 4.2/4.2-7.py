a = int(input())
b = int(input())
c = int(input())

x1 = a + b > c
x2 = a + c > b
x3 = b + c > a

if x1 and x2 and x3:
	print('YES')
else:
	print('NO')