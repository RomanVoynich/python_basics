num = int(input())

if num % 2 != 0:
	print('YES')
else:
	if (num >= 2 and num <= 5) and (num % 2 == 0):
		print('NO')
	elif (num >= 6 and num <= 20) and (num % 2 == 0):
		print('YES')
	elif num > 20 and num % 2 == 0:
		print('NO')
	else:
		print('NO')
