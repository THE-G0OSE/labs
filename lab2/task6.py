arr = []
for x in range(10):
    arr.append(input('введите элемент списка(всего 10)\n'))
del arr[3:8]
for x in range(2):
    arr.append(input('введите новый элемент(всего 2)'))
print(' '.join(arr))
