# word = input()
# if word == 'Python':
#    print("It's OK")
# else:
#    print("Nooo it's not OK")

# num = int(input())
# num1 = num % 10
# num2 = num // 10
#
# if num1 == num2:
#    print('the numbers are equal')
# else:
#    print('the numbers it is not are equal')

num1, num2, num3 = int(input()), int(input()), int(input())
count = 0

if num1 % 2 == 0:
    count = count + 1
if num2 % 2 == 0:
    count = count + 1
if num3 % 2 == 0:
    count = count + 1
print(num1, num2, num3)
print(count)
