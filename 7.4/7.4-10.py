num = int(input())
num2 = num
count = 0

while num != 0:
	last = num % 10
	num //= 10
	count += 1

for i in range(count - 1):
	last1 = num2 % 10
	num2 //= 10
print(last1)
