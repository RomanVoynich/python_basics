n = int(input())

while n != 0:
	last_digit = n % 10
	n = n // 10
	print('n = ', n, 'last digit = ', last_digit)
print(n, last_digit)
