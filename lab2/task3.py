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
        

