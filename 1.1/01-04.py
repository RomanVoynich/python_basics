import random
a = random.randrange(1, 10)
b = random.randrange(1, 10)
answer = input(f'{a}+{b}=')
if answer.isdigit():
    if int(answer) == a + b:
        print('its ok')
    else:
        print('its not ok')
else:
    print('enter number')
