num = int(input())
total = 0
count = 0
products = 1
first = num % 10


while num != 0:
	last = num % 10
	num //= 10
	total += last
	count += 1
	products *= last

print(total)
print(count)
print(products)
print(total / count)
print(last)
print(first + last)



