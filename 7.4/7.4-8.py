num = int(input())
mx = 0
mn = 9

while num != 0:
	last = num % 10
	num //= 10
	if last > mx:
		mx = last
	if last < mn:
		mn = last
		
	

print(mx)
print(mn)
