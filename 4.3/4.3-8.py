column = int(input())
row = int(input())

column1 = int(input())
row1 = int(input())


if (column % 2 == 0 and row % 2 == 0) or (column % 2 != 0 and row % 2 != 0):
	a = 'white'
else:
	a = 'black'

if (column1 % 2 == 0 and row1 % 2 == 0) or (column1 % 2 != 0 and row1 % 2 != 0):
	a1 = 'white'
else:
	a1 = 'black'

if a == a1:
	print('YES')
else:
	print('NO')
