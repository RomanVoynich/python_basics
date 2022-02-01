x = int(input())
y = int(input())

if x >= 0 and y <= 0:
    print("It's 1 quarter")
if x >= 0 and y >= 0:
    print("It's 2 quarter")
if x <= 0 and y <= 0:
    print("It's 3 quarter")
if x <= 0 and y >= 0:
    print("It's 4 quarter")
