# maximum and minimum
n = int(input())

largest = -1
larges2 = -1
for i in range(n):
	num = int(input())
	if num > largest:
		largest = num
		if larges2 < num:
			largest, larges2 = larges2, largest


print(larges2)
print(largest)
