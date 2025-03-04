a = input('введите число А\n')
b = input('введите число B\n')
h = input('введите число H\n')

if h > b:
    print('Пересып') 
elif h < a:
    print('Недосып')
else:
    print('Это нормально')
