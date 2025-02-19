number = input('Введите номер\n')
letterIndexes = [0, 4, 5]
numIndexes = [1, 2, 3, 6, 7, 8]
letters = 'авекмнорстух'
nums = '1234567890'
correct = True
if len(number) != 8 and len(number) != 9:
    correct = False
else:
    for i in letterIndexes:
        if number[i].lower() not in letters:
            correct = False
    if len(number) == 8:
        for i in numIndexes[: -1]:
            if number[i].lower() not in nums:
                correct = False
    else:
        for i in numIndexes:
            if number[i].lower() not in nums:
                correct = False
print('Номер введён корректно' if correct else 'Номер введён некорректно')