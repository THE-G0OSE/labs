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