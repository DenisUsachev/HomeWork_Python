"""Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
"""

import random

array = [random.randrange(10) for _ in range(int(input('Введите количество чисел в массиве: ')))]
num = int(input('Введите число: '))
near_num = 0
diff = 1

while near_num == 0 :
    for i in range(len(array)):
        if array[i] - num == diff or num - array[i] == diff:
            near_num = array[i]
            break
    else:
        diff += 1

print(array)
print(near_num)