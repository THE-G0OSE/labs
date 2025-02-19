arr = list(map(int, input('Введите числа разделяя пробелами\n').split(' ')))
answer = 0
for i in range(len(arr)):
    if arr[i] < 10:
        answer+=arr[i]
print(answer)