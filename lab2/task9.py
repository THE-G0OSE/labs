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