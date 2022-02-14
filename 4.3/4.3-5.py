num1 = int(input())
num2 = int(input())
operator = input()

if operator == '/' and num2 == 0:
	print('!!! 0 !!!')
else:
	if operator == '+':
		print(num1 + num2)
	elif operator == '-':
		print(num1 - num2)
	elif operator == '*':
		print(num1 * num2)
	elif operator == '/':
		print(num1 / num2)
	else:
		print('NO OPERATOR')
