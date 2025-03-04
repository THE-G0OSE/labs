cost = int(input('введите цену\n'))

for i in range(1, 11):
    print('цена ' + str(i) + ' кг конфет:', cost * i, ' руб')