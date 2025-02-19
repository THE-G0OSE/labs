string = input('введите строку\n')
answer = ''
for x in string:
    if x.lower() == 'л':
       answer += x 
print(answer)