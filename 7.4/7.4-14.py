num = int(input())
total = 0
for i in range(2, num + 1):
	if num % i == 0:
		total = i
		break
print(total)
