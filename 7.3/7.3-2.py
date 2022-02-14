n = int(input())

num1 = 0
temp = 0
num2 = 0

for i in range(n):
	num = int(input())
	if num > num1:
		num1 = num
		temp = num
	if num > temp:
		num2 = num
print(num1)
print(num2)
print(temp)
# поменять переменные местами