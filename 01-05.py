# determine the number of tens and ones in a two-digit number
num = int(input())
# a = num % 10
# b = num // 10
# print(a, b, sep='|')
# print('number :', a * 100 + b)
a = num % 10
b = (num % 100) // 10
c = (num % 1000) // 100
d = num // 1000
print(a, b, c, d, sep='|')
