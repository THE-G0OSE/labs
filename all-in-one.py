import lab1
import lab2
import lab3

import prettytable

isContinue = True

labsTable = prettytable.PrettyTable()

labsTable.field_names = ['Номер', 'Название']
labsTable.add_rows([[1, 'Введение в Python, математические операции'], [2, 'Строки и списки'], [3, 'Логические операции, условные конструкции и циклы Python']])
labsTable.align = 'l'
labsTable.align['Номер'] = 'c'

lab1Table = prettytable.PrettyTable()

lab1Table.field_names = ['Номер', 'Название']
lab1Table.add_rows([[1, 'диалог'], [2, 'пример'], [3, 'все чётные элементы'], [4, 'умножение всех чисел меньше 10'], [5, 'среднее арифметическое']])
lab1Table.align = 'l'
lab1Table.align['Номер'] = 'c'

lab2Table = prettytable.PrettyTable()
lab2Table.field_names = ['Номер', 'Название']
lab2Table.add_rows([[1, 'Ввод числа пока оно совпадает с загаданным'],[2, 'слова размером от 5 до 10'],[3, 'вывод строк заканчивающихся на r'],[4, 'генерация строки'],[5, 'строка содержащая только буквы Л'],[6, 'удалить с 4 по 8 добавить 2'],[7, 'табличка'],[8, 'отфильтрованная табличка'],[9, 'футбольная команда'],[10, 'валидация номера'],[11, 'сортировка']])
lab2Table.align = 'l'
lab2Table.align['Номер'] = 'c'

lab3Table = prettytable.PrettyTable()
lab3Table.field_names = ['Номер', 'Название']
lab3Table.add_rows([[1, 'минимальное число'],[2, 'режим сна'],[3, 'високосный год'],[4, 'интервалы'],[5, 'счастливый билет'],[6, 'сумма'],[7, 'НОК'],[8, 'вывод чисел от 10 до 100'],[9, 'стоимость конфет'],[10, 'сумма и количество всех чисел последовательности']])
lab3Table.align = 'l'
lab3Table.align['Номер'] = 'c'

while isContinue:
    print(labsTable)
    labnum = int(input('Введите номер лабораторной работы\n'))
    if labnum == 1:
        print(lab1Table) 
        tasknum = int(input('Введите номер задания\n'))
        if tasknum == 1:
            lab1.task1()
        elif tasknum == 2:
            lab1.task2()
        elif tasknum == 3:
            lab1.task3()
        elif tasknum == 4:
            lab1.task4()
        elif tasknum == 5:
            lab1.task5()
    elif labnum == 2:
        print(lab2Table) 
        tasknum = int(input('Введите номер задания\n'))
        if tasknum == 1:
            lab2.task1()
        elif tasknum == 2:
            lab2.task2()
        elif tasknum == 3:
            lab2.task3()
        elif tasknum == 4:
            lab2.task4()
        elif tasknum == 5:
            lab2.task5()
        elif tasknum == 6:
            lab2.task6()
        elif tasknum == 7:
            lab2.task7()
        elif tasknum == 8:
            lab2.task8()
        elif tasknum == 9:
            lab2.task9()
        elif tasknum == 10:
            lab2.task10()
        elif tasknum == 11:
            lab2.task11()
    elif labnum == 3:
        print(lab3Table) 
        tasknum = int(input('Введите номер задания\n'))
        if tasknum == 1:
            lab3.task1();
        elif tasknum == 2:
            lab3.task2();
        elif tasknum == 3:
            lab3.task3();
        elif tasknum == 4:
            lab3.task4();
        elif tasknum == 5:
            lab3.task5();
        elif tasknum == 6:
            lab3.task6();
        elif tasknum == 7:
            lab3.task7();
        elif tasknum == 8:
            lab3.task8();
        elif tasknum == 9:
            lab3.task9();
        elif tasknum == 10:
            lab3.task10();
    cont = input('Продолжаем?\nВведите "да" или "нет"')
    if cont == 'да' or cont == 'д' or cont == 'y':
        isContinue = True
    elif cont == 'нет' or cont == 'н' or cont == 'n':
        isContinue = False
    