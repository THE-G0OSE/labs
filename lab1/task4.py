arr = list(map(int, input('Введите числа разделяя пробелами\n').split(' ')))
answer = 0
notZero = True
for i in range(len(arr)):
    if arr[i] == 0:
        notZero = False
    elif arr[i] < 10:
        if answer == 0:
            answer+=arr[i]
        else: 
            answer *= arr[i]
print(answer if notZero else 0)