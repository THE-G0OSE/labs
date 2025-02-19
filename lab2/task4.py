import random
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a = ''
correct = False
ind = 0
for x in range(6): 
    a += random.choice(nums)
if '3' in a:
    correct = True
while not(correct):
    a = a[:ind] + random.choice(nums) + a[ind + 1:]
    if '3' in a:
        correct = True
        break
    ind += 1
    if ind > 5:
        ind = 0
print(a)