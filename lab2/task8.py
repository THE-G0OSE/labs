from prettytable import PrettyTable
table = PrettyTable()
string = 'ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса'
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
table.align = 'l'
print(table)
