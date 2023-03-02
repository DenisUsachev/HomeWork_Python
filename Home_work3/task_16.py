"""16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
   В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
"""

import random

array = [random.randrange(10) for _ in range(int(input('Введите количество чисел в массиве: ')))]
quantity_num = int(input('Введите число которое будет считать: '))
count = 0

for i in range(len(array)):
    if array[i] == quantity_num:
        count += 1
print(array)
print(count)