answer = 0
while True:
    a = int(input('введите число или 0 если хотитие закончить ввод\n'))
    if a == 0:
        break
    else:
        answer += a
print(answer)
