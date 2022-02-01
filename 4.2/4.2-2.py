num = int(input())
a = num // 100
b = (num % 100) // 10
c = num % 10

if a != b and a != c and b != c:
    print("It's different numbers")
else:
    print("It's no different numbers")
