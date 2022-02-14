num = int(input())
flag = False

while num != 0:
	last_digit = num % 10
	if last_digit == 7:
		flag = True
	num = num // 10

if flag:
	print('yes')
else:
	print('No')
