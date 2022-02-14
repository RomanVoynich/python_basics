# counter with two variables

num = int(input())

count1 = 0
count2 = 0

for i in range(10):
	num = int(input())
	if num > 10:
		count1 = count1 + 1
	if num == 0:
		count2 = count2 + 1
print('count1 = ', count1)
print('count2 = ', count2)

