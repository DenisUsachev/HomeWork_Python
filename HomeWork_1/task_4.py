x = int(input('Введите длинну плитки: '))
y = int(input('Введите ширину плитки: '))
k = int(input('Сколько долек хотите отломить: '))

if k % x == 0 or k % y == 0: print('Yes')
else: print('No')