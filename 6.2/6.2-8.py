c1 = input()
c2 = input()
c3 = input()

mn = min(len(c1), len(c2), len(c3))
mx = max(len(c1), len(c2), len(c3))

if len(c1) == mn:
	print(c1)
elif len(c2) == mn:
	print(c2)
elif len(c3) == mn:
	print(c3)

if len(c1) == mx:
	print(c1)
elif len(c2) == mx:
	print(c2)
elif len(c3) == mx:
	print(c3)



