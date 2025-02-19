import random
my_number = round(random.random() * 100)
a = my_number
while a == my_number:
    a = input('введите число отличное от загаданного\n')
print('Отлично, загаданное число было равно ', my_number)