num = int(input())
count = 0

coin1 = 25
coin2 = 10
coin3 = 5
coin4 = 1

while not(num == 0):
    if num >= coin1:
        num -= coin1
        count += 1
    if coin2 <= num < coin1:
        num -= coin2
        count += 1
    if coin3 <= num < coin2:
        num -= coin3
        count += 1
    if coin4 <= num < coin3:
        num -= coin4
        count += 1
print(count)
