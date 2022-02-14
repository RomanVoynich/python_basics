color1 = str(input())
color2 = str(input())

red = 'red'
blue = 'blue'
yellow = 'yellow'

if color1 == red and color2 == red:
    print(red)
elif color1 == blue and color2 == blue:
    print(blue)
elif color1 == yellow and color2 == yellow:
    print(yellow)
elif (color1 == red and color2 == blue) or (color1 == blue and color2 == red):
    print('purple')
elif (color1 == red and color2 == yellow) or (color1 == yellow and color2 == red):
    print('orange')
elif (color1 == blue and color2 == yellow) or (color1 == yellow and color2 == blue):
    print('green')
else:
    print('NO COLOR')
