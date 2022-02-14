a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())

x = a + b
x1 = a1 + b1

if (x + 3 == x1) or (x - 3 == x1):
	print('YES')
elif (x + 1 == x1) or (x - 1 == x1):
	print('YES')
else:
	print('NO')