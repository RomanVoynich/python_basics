a = int(input())
b = int(input())
c = int(input())

if (b < a < c) or (b > a > c):
	print(a)
elif (a < b < c) or (a > b > c):
	print(b)
elif (a < c < b) or (a > c > b):
	print(c)
