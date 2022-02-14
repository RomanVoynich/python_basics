num = int(input())

for i in range(1, num + 1):
    if i >= 5 and i <= 9:
        continue
    if i >= 17 and i <= 37:
        continue
    if i >= 78 and i <= 87:
        continue
    print(i)
