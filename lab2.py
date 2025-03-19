def task1():
    import random
    my_number = round(random.random() * 100)
    a = my_number
    while a == my_number:
        a = input('введите число отличное от загаданного\n')
    print('Отлично, загаданное число было равно ', my_number)

def task2():
    string = input('введите строку\n')
    string = string.replace('.', ' ').replace(',' , ' ').replace(':', ' ').replace(';', ' ')
    arr = string.split(' ')
    answer = [] 
    for x in arr:
        if len(x) > 5 and len(x) < 10:
             answer.append(x)   
    print(' '.join(answer))

def task3():
    a = ''
    arr = []
    while a != '.':
        a = input('введите строку или \'.\' если хотите закончить ввод\n')
        if a == '.': 
            break
        else:
            arr.append(a)
    for a in arr:
        if a[-1] == 'r':
            print(a)
        
def task4():
    import random
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    a = ''
    correct = False
    ind = 0
    for x in range(6): 
        a += random.choice(nums)
    if '3' in a:
        correct = True
    while not(correct):
        a = a[:ind] + random.choice(nums) + a[ind + 1:]
        if '3' in a:
            correct = True
            break
        ind += 1
        if ind > 5:
            ind = 0
    print(a)

def task5():
    string = input('введите строку\n')
    answer = ''
    for x in string:
        if x.lower() == 'л':
            answer += x 
    print(answer)

def task6():
    arr = []
    for x in range(10):
        arr.append(input('введите элемент списка(всего 10)\n'))
    del arr[3:8]
    for x in range(2):
        arr.append(input('введите новый элемент(всего 2)'))
    print(' '.join(arr))

def task7():
    from prettytable import PrettyTable
    table = PrettyTable()
    string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'
    rows = string.split('_')
    headersRaw = rows[0].split(';')
    headers = headersRaw[:3]
    headers.append('О студенте')
    table.field_names = headers[:4]
    for i in rows[1:]:
        row = i.split(';')
        table.add_row([row[0],row[1],row[2],' '.join(row[3:5])])
    table.border = False
    table.align = 'l'
    table.align['О студенте'] = 'c'
    print(table)    

def task8():
    from prettytable import PrettyTable
    table = PrettyTable()
    string = 'ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса'
    rows = string.split('_')
    def notnull(i):
        return True if i != '' else False
    table.field_names = filter( notnull, rows[0].split(';'))
    rows = [list(filter(notnull, i.split(';'))) for i in rows]
    rightRows = []
    for i in range(1, len(rows)):
        if int(rows[i][1][:2]) > 21:
            rightRows.append(rows[i])
    table.add_rows(rightRows)
    table.border = False
    table.align = 'l'
    print(table)

def task9():
    letters1 = 'уеыаоэяиюё'
    letters2 = 'йцкнгшщзхфвпрлджчсмтб'
    name = input('Введите название команды\n')
    counter1 = 0
    counter2 = 0
    for i in name:
        if i.lower() in letters1:
            counter1 += 1
        elif i.lower() in letters2:
            counter2 += 1
    print('Футбольная команда ' + name + ' имеет длину ' + str(len(name)) + ' символов, колличество согласных букв = ' + str(counter2) + ', количество гласных букв = ' + str(counter1) + '.') 

def task10():
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

def task11():
    arr = []
    for i in range(3): 
        arr.append(input('Введите слово\n')) 
    arr = sorted(arr)
    print(' '.join(arr))
