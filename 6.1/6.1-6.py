num = int(input())
a = num // 100
b = (num // 10) % 10
c = num % 10
mn = min(a, b, c)
mx = max(a, b, c)
md = (a + b + c) - (mn + mx)
if (mx - mn) == md:
	print('beautiful')
else:
	print('ugly')
