string = input('введите строку\n')
string = string.replace('.', ' ').replace(',' , ' ').replace(':', ' ').replace(';', ' ')
arr = string.split(' ')
answer = [] 
for x in arr:
    if len(x) > 5 and len(x) < 10:
       answer.append(x)   
print(' '.join(answer))