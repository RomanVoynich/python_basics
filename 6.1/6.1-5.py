a = int(input())
b = int(input())
c = int(input())

mn = min(a, b, c)
mx = max(a, b, c)

if (a != b and a != c) and (b != a and b != c) and (c != a and c != b):
    if mn != a and mx != a:
        ar = int(a)
    elif mn != b and mx != b:
        ar = int(b)
    elif mn != c and mx != c:
        ar = int(c)
else:
    if a == b or a == c:
        ar = a
    elif b == a or b == c:
        ar = b
    elif c == a or c == b:
        ar = c


print('max', mx)
print('avr', ar)
print('min', mn)
