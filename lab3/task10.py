arr = list(map(int, input('введите все числа отделяя их пробелами\n').split()))

a = 0

Sum = 0

count = 1

while True:
    if arr[a] == 0:
        break
    else:
        Sum += arr[a]
        count += 1
    a += 1
print('сумма всех чисел:', Sum, 'кол-во чисел:', count)