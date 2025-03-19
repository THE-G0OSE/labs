def task1():
    name = input('Как вас зовут?\n')
    university = input('Укажите название ВУЗа, в котором вы обучаетесь\n')
    group = input('Номер вашей группы\n')
    language = input('Какой язык программирования вы начинаете изучать?\n')
    print('Добрый день, ' + name)
    print('Вы обучаетесь в образовательной организации ' + university + ' в группе ' + group)
    print(name + ', желаем вам успешного обучения программированию на языке ' + language)

def task2():
    a = int(input('Введите a\n'))
    b = int(input('Ввeдите b\n'))
    c = int(input('Введите c\n'))
    answer = 0
    try:
    
        def divide(a, b):
            if b == 0:
                raise ValueError('Деление на ноль')
            else:
                return a / b 
    
        answer = 1 - a*b - a*(b**2 - c**2) + (b - c + a) * divide((12 + b), (c-a))
    
        if answer < 0:
            answer = answer * -1
        print(answer)
    except ValueError as e:
        print(e)

def task3():
    arr = input('Введите все элементы массива разделяя их пробелами\n').split(' ')
    answer = []
    print('чётные элементы:')
    for x in range(0, len(arr)):
        if x & 1 == 1:
            answer.append(arr[x])
    print(' '.join(answer))

def task4():
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

def task5():
    arr = list(map(int, input('Введите все числа разделяя пробелами\n').split(' ')))
    print(sum(arr) / len(arr))