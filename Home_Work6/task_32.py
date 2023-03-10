""" Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)"""

n = int(input('Введите разверность массива: '))
arr = []
for i in range(n):
    arr.append(int(input(f'Введите {i + 1} число: ')))
print(arr)

min_a = int(input('Введите минимум: '))
max_a =int(input('Введите максимум: '))
arr2 = []

for j in range(len(arr)):
    if min_a < arr[j] < max_a:
        arr2.append(j)

print(arr2)