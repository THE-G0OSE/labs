def task1():
    a = input('Введите число А\n')
    b = input('Введите число B\n')
    c = input('Введите число C\n')

    answer = a
    
    if answer > b:
        answer = b

    if answer > c:
        answer = c

    print('наименьшее число: ', answer)

def task2():
    a = input('введите число А\n')
    b = input('введите число B\n')
    h = input('введите число H\n')

    if h > b:
        print('Пересып') 
    elif h < a:
        print('Недосып')
    else:
        print('Это нормально')

def task3():
    year = int(input('введите год\n'))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Високостный')
    else:
        print('Обычный')

def task4():
    num = int(input('Введите число\n'))

    if (num > -15 and num <= 12) or (num > 14 and num < 17) or num >= 19:
        print('True')
    else:
        print('False')

def task5():
    num = input('введите номер билета\n')

    firstHalf = sum(list(map(int, list(num)))[:3])
    secondHalf = sum(list(map(int, list(num)))[3:])

    if firstHalf == secondHalf:
        print('Счастливый')
    else: 
        print('Обычный')
    
def task6():
    answer = 0
    while True:
        a = int(input('введите число или 0 если хотитие закончить ввод\n'))
        if a == 0:
            break
        else:
            answer += a
    print(answer)

def task7():

    def NOD(n1, n2):
        if n1 == n2:
            return n1
        else:
            d = max(n1, n2) - min(n1, n2) 
            div = NOD(min(n1, n2), d)
        return div

    a = int(input('введите первое число\n'))
    b = int(input('введите второе число\n'))
    if a == b: 
        print(a)
    else: 

        answer = a * b / NOD(a, b)

        print(answer)

def task8():
    answer = []
    while True:
        a = int(input('введите число\n'))
        if a > 100:
            break
        elif a >= 10:
            answer.append(a)
    print(answer)

def task9():
    cost = int(input('введите цену\n'))

    for i in range(1, 11):
        print('цена ' + str(i) + ' кг конфет:', cost * i, ' руб')

def task10():
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