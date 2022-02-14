name = input('input your name : ')
age = input("your age : ")

# simple print
#print('Your name is ' + name + ' and you have ' + age + ' age')
#print('Your name have '+str(len(name))+' letters')

# concatenation operator
greet = 'yor name is ' + name
greet += ' and you have ' + age + ' age'
print(greet)
