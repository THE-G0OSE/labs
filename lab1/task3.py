arr = input('Введите все элементы массива разделяя их пробелами\n').split(' ')
print('чётные элементы:')
for x in range(0, len(arr)):
    if x & 1 == 1:
        print(arr[x])
