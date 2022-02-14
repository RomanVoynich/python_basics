num = int(input())
num2 = num
count = 0
answer = 'YES'
a = 0

while num != 0:
	last = num % 10
	num //= 10
	count += 1
	a = last
for i in range(count - 1):
	last = num2 % 10
	num2 //= 10
	if last >= a:
		answer = 'NO'


print(answer)



