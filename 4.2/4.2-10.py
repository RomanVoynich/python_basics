column = int(input())
row = int(input())

column1 = int(input())
row1 = int(input())

if (column1 == column) or (column1 == column + 1) or (column1 == column - 1):
    a = True
else:
    a = False

if (row1 == row) or (row1 == row + 1) or (row1 == row - 1):
    b = True
else:
    b = False

if a is True and b is True:
    print('YES')
else:
    print("NO")
