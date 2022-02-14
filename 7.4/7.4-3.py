num = int(input())
count = 0

while not(num < 0) and num > 5:
	num = int(input())
	if num == 5:
		count += 1
print(count)
