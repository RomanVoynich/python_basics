a = len(input())
b = len(input())
c = len(input())

mn = min(a, b, c)
mx = max(a, b, c)
md = (a + b + c) - (mn + mx)

a = mn
b = md
c = mx

if (b - a) == (c - b):
	print('YES')
else:
	print('NO')
