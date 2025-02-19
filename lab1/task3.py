arr = input('Введите все элементы массива разделяя их пробелами\n').split(' ')
answer = []
print('чётные элементы:')
for x in range(0, len(arr)):
    if x & 1 == 1:
        answer.append(arr[x])
print(' '.join(answer))