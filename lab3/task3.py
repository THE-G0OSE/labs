year = int(input('введите год\n'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Високостный')
else:
    print('Обычный')