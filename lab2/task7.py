from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ['Ф', 'И', 'О', 'о студенте']
table.add_row(['Иванов', 'Иван', 'Иванович', 'Студент 3 курса, 23 года'])
table.add_row(['Петров', 'Семен', 'Игоревич', 'Студент 2 курса, 22 года'])
table.border = False
table.align = 'l'
print(table)