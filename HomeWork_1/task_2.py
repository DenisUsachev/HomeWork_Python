# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

number_products = int(input('Введите сколько было сделано журавликов: '))


first_child = number_products // 4
third_child = number_products // 4
second_child = number_products - first_child - third_child

print(first_child, second_child, third_child)