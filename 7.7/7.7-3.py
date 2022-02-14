n = int(input())

max_digit = 0

while n != 0:
    digit = n % 10
    if digit % 3 == 0 and digit > max_digit:
        digit = max_digit
    n //= 10
    print(digit)

if max_digit == 0:
    print('NO')
else:
    print(max_digit)
