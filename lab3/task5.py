num = input('введите номер билета\n')


firstHalf = sum(list(map(int, list(num)))[:3])
secondHalf = sum(list(map(int, list(num)))[3:])

if firstHalf == secondHalf:
    print('Счастливый')
else: 
    print('Обычный')