num = int(input())

if num >= 0 and num <= 36:

    if num % 2 == 0 and (num >= 1 and num <= 10):
        print('black')
    elif num % 2 != 0 and (num >= 11 and num <= 18):
        print('black')
    elif num % 2 == 0 and (num >= 19 and num <= 28):
        print('black')
    elif num % 2 != 0 and (num >= 29 and num <= 36):
        print('black')
    elif num == 0:
        print('green')

    else:
        print("red")

else:

    print('INPUT ERROR')
