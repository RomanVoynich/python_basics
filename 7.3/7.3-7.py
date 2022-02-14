# signal lables

# program that determines that a natural number is prime

num = int(input())
flag = True

for i in range(2, num):
	if num % i == 0:
		flag = False

if num == 1:
	print('It is ONE, that it is not prime and not composite')
elif flag is True:
	print('It is prime number')
else:
	print('It is composite number')
