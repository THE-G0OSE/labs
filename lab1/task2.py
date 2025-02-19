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