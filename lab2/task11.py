arr = []
for i in range(3): 
    arr.append(input('Введите слово\n')) 
arr = sorted(arr)
print(' '.join(arr))